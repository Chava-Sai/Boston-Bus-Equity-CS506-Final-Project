# bus_equity/model_pipeline.py

from __future__ import annotations

from pathlib import Path
from typing import Tuple, Dict, Any

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import xgboost as xgb


# IMPORTANT: your path is data/arr_dep_demo.csv
DEFAULT_DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "arr_dep_demo.csv"
)


def load_arr_dep_demo(path: Path | str = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """
    Load the demo arrival/departure + demographics dataset used
    for the lateness prediction model.
    """
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("arr_dep_demo.csv loaded but is empty")

    expected_cols = {
        "route_id",
        "stop_id",
        "lateness",
        "scheduled_headway",
        "time_point_order",
        "earliness",
        "actual",
        "scheduled",
        "point_type",
        "standard_type",
        "direction",
        "pct_white",
        "pct_black",
        "pct_asian",
        "pct_hispanic",
    }
    missing = expected_cols.difference(df.columns)
    if missing:
        raise ValueError(f"arr_dep_demo.csv is missing columns: {missing}")

    return df


def build_feature_matrix(
    df_raw: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.Series, list[str]]:
    """
    Feature engineering to get X (features) and y (target lateness)
    in a form suitable for XGBoost, matching the spirit of your notebook.
    """
    df = df_raw.copy()

    # --- 1. Parse times ---
    for col in ["actual", "scheduled"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    # Drop rows with no target or no scheduled time
    df = df.dropna(subset=["lateness", "scheduled"]).copy()

    # --- 2. Temporal features ---
    df["scheduled_hour"] = df["scheduled"].dt.hour
    df["scheduled_minute"] = df["scheduled"].dt.minute
    df["scheduled_sec"] = (
        df["scheduled"].dt.hour * 3600
        + df["scheduled"].dt.minute * 60
        + df["scheduled"].dt.second
    )

    # --- 3. Fill numeric NaNs with medians ---
    numeric_cols = [
        "scheduled_headway",
        "time_point_order",
        "earliness",
        "pct_white",
        "pct_black",
        "pct_asian",
        "pct_hispanic",
        "scheduled_hour",
        "scheduled_minute",
        "scheduled_sec",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].astype(float)
            df[col] = df[col].fillna(df[col].median())

    # --- 4. Categorical → one-hot ---
    cat_cols = []
    if "point_type" in df.columns:
        cat_cols.append("point_type")
    if "direction" in df.columns:
        cat_cols.append("direction")

    if cat_cols:
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    # --- 5. Build X, y ---
    y = df["lateness"].astype(float)

    drop_cols = [
        "lateness",
        "actual",
        "scheduled",
        "route_id",
        "stop_id",
        "standard_type",
    ]
    feature_df = df.drop(columns=[c for c in drop_cols if c in df.columns])

    # Sanity: no NaNs in feature matrix
    if feature_df.isna().any().any():
        raise ValueError("Feature matrix contains NaNs after preprocessing")

    feature_cols = list(feature_df.columns)
    return feature_df, y, feature_cols


def train_xgb_regressor(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> xgb.XGBRegressor:
    """
    Train an XGBoost regressor with reasonable defaults for this dataset.
    """
    model = xgb.XGBRegressor(
        n_estimators=200,
        max_depth=4,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="reg:squarederror",
        random_state=42,
        n_jobs=4,
    )
    model.fit(X_train, y_train)
    return model


def evaluate_model(
    model: xgb.XGBRegressor,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> Dict[str, Any]:
    """
    Compute RMSE and R^2 on both train and test sets.
    Implemented in a way that works across sklearn versions
    (no reliance on `squared` kwarg).
    """
    pred_train = model.predict(X_train)
    pred_test = model.predict(X_test)

    # mean_squared_error returns MSE; take sqrt for RMSE
    mse_train = mean_squared_error(y_train, pred_train)
    mse_test = mean_squared_error(y_test, pred_test)
    rmse_train = mse_train ** 0.5
    rmse_test = mse_test ** 0.5

    r2_train = r2_score(y_train, pred_train)
    r2_test = r2_score(y_test, pred_test)

    return {
        "rmse_train": rmse_train,
        "rmse_test": rmse_test,
        "r2_train": r2_train,
        "r2_test": r2_test,
    }


def train_and_evaluate(
    csv_path: Path | str = DEFAULT_DATA_PATH,
    test_size: float = 0.2,
    random_state: int = 42,
) -> Dict[str, Any]:
    """
    Convenience function used by tests:
    loads data, builds features, splits train/test, trains XGB,
    and returns metrics.
    """
    df = load_arr_dep_demo(csv_path)
    X, y, feature_cols = build_feature_matrix(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = train_xgb_regressor(X_train, y_train)
    metrics = evaluate_model(model, X_train, y_train, X_test, y_test)
    metrics["n_train"] = len(X_train)
    metrics["n_test"] = len(X_test)
    metrics["n_features"] = len(feature_cols)
    return metrics
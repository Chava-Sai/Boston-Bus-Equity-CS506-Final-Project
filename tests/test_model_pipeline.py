# tests/test_model_pipeline.py

# tests/test_model_pipeline.py

from pathlib import Path
import os
import sys
import numpy as np
import pandas as pd

# --- Make sure repo root is on sys.path ---
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from bus_equity.model_pipeline import (
    load_arr_dep_demo,
    build_feature_matrix,
    train_and_evaluate,
)

DATA_PATH = ROOT_DIR / "data" / "arr_dep_demo.csv"


def test_demo_csv_loads_and_has_expected_columns():
    df = load_arr_dep_demo(DATA_PATH)
    assert not df.empty

    for col in [
        "route_id",
        "stop_id",
        "lateness",
        "scheduled_headway",
        "time_point_order",
        "earliness",
        "actual",
        "scheduled",
        "pct_white",
        "pct_black",
        "pct_asian",
        "pct_hispanic",
    ]:
        assert col in df.columns


def test_feature_matrix_shapes_and_cleanliness():
    df = load_arr_dep_demo(DATA_PATH)
    X, y, feature_cols = build_feature_matrix(df)

    assert len(X) == len(y)
    assert len(feature_cols) == X.shape[1]

    # No NaNs in features
    assert not X.isna().any().any()

    # Lateness should be finite
    assert np.isfinite(y).all()

    # Some important engineered features should exist
    for col in ["scheduled_headway", "time_point_order", "scheduled_hour"]:
        assert col in X.columns


def test_model_performance_on_demo_sample():
    """
    Sanity-check that the model actually learns something.
    Thresholds are relaxed — we just don't want a totally broken model.
    """
    metrics = train_and_evaluate(DATA_PATH, test_size=0.2, random_state=42)

    assert metrics["n_train"] > 0
    assert metrics["n_test"] > 0
    assert metrics["n_features"] > 5

    # Lateness is in minutes, so RMSE shouldn't be huge
    assert metrics["rmse_test"] < 2.5

    # Model should explain some variance
    assert metrics["r2_test"] > 0.3
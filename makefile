PYTHON=python
VENV=.venv

install:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/Scripts/pip install --upgrade pip || $(VENV)/bin/pip install --upgrade pip
	$(VENV)/Scripts/pip install -r requirements.txt || $(VENV)/bin/pip install -r requirements.txt

clean:
	rm -rf $(VENV)

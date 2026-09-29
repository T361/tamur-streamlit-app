#!/bin/sh
# setup.sh - creates a virtual environment and downloads all libraries
# required by the Streamlit app (streamlit_app.py).
set -e
cd "$(dirname "$0")"

PY=python3
if ! command -v "$PY" >/dev/null 2>&1; then
    PY=python
fi

if [ ! -d ".venv" ]; then
    echo "[setup] Creating virtual environment: .venv"
    "$PY" -m venv .venv
fi

echo "[setup] Activating virtual environment"
. .venv/bin/activate

echo "[setup] Upgrading pip"
python -m pip install --upgrade pip

echo "[setup] Downloading libraries from requirements.txt"
python -m pip install -r requirements.txt

echo "[setup] Done. Start the app with: ./run.sh"

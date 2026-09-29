#!/bin/sh
# run.sh - starts the Streamlit app (streamlit_app.py).
cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
    echo "[run] Virtual environment missing - downloading libraries first..."
    ./setup.sh
fi

. .venv/bin/activate
streamlit run streamlit_app.py

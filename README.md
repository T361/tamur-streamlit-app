# Streamlit Pathfinding Visualizer

Interactive visualization of **Greedy Best-First Search (GBFS)** and **A\*** pathfinding algorithms, built with Streamlit and NetworkX.

## Features

- Choose the start node from a dropdown menu
- Choose the goal node from a dropdown menu
- Select the search algorithm: **GBFS** or **A\***
- Visualize the hospital graph with NetworkX, with the solution path highlighted
- View the algorithm, expansion order, solution path, and total path cost

## Run Locally

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy to Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and click **New app**.
3. Select this GitHub repository, branch `main`, and main file `streamlit_app.py`.
4. Click **Deploy** — Streamlit Cloud installs `requirements.txt` automatically.

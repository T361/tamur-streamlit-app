# Tamur Streamlit App

Interactive visualization of **Greedy Best-First Search (GBFS)** and **A\*** pathfinding algorithms, built with Streamlit and NetworkX (Lab 06).

## Features

- Choose the start node from a dropdown menu
- Choose the goal node from a dropdown menu
- Select the search algorithm: **GBFS** or **A\***
- Visualize the graph with NetworkX, with the solution path highlighted
- View the algorithm, solution path, expansion order, and total path cost

## Run the App

```sh
./run.sh
```

`run.sh` installs all dependencies into a virtual environment automatically on the first run (via `setup.sh`).

Or manually:

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Files

| File               | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| `streamlit_app.py` | The Streamlit GUI and GBFS/A* implementations  |
| `lab06.ipynb`      | Lab notebook with the underlying tasks         |
| `requirements.txt` | Python dependencies                            |
| `setup.sh`         | Creates a venv and downloads all libraries     |
| `run.sh`           | Starts the Streamlit app                       |
| `run.txt`          | One-line command to run the Streamlit app      |

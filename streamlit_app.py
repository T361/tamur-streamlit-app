import streamlit as st
import math
import heapq
import networkx as nx
import matplotlib.pyplot as plt

locations = {
    "Pharmacy": (0, 0),
    "Main_Corridor": (2, 1),
    "Patient_Wing": (1, 4),
    "Nursing_Station": (4, 2),
    "Laboratory": (5, 5),
    "Emergency_Ward": (8, 6)
}

hospital_graph = {
    "Pharmacy": {"Main_Corridor": 2.2, "Patient_Wing": 4.1},
    "Main_Corridor": {"Nursing_Station": 2.2},
    "Patient_Wing": {"Laboratory": 5.0},
    "Nursing_Station": {"Laboratory": 3.2, "Emergency_Ward": 6.0},
    "Laboratory": {"Emergency_Ward": 3.2},
    "Emergency_Ward": {}
}

def heuristic(current, goal):
    x1, y1 = locations[current]
    x2, y2 = locations[goal]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def reconstruct_path(came_from, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path

def gbfs(start, goal):
    counter = 0
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), counter, start))
    came_from = {start: None}
    visited = set()
    expansion_order = []

    while open_set:
        _, _, current = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        expansion_order.append(current)
        if current == goal:
            break
        for neighbor in hospital_graph.get(current, {}):
            if neighbor not in visited:
                counter += 1
                heapq.heappush(open_set, (heuristic(neighbor, goal), counter, neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current

    if goal not in came_from:
        return None, None, None

    path = reconstruct_path(came_from, goal)
    cost = sum(hospital_graph[path[i]][path[i+1]] for i in range(len(path) - 1))
    return path, cost, expansion_order

def a_star(start, goal):
    counter = 0
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), counter, start))
    came_from = {start: None}
    g_cost = {start: 0}
    expansion_order = []
    closed = set()

    while open_set:
        f, _, current = heapq.heappop(open_set)
        if current in closed:
            continue
        closed.add(current)
        expansion_order.append(current)
        if current == goal:
            break
        for neighbor, cost in hospital_graph.get(current, {}).items():
            if neighbor in closed:
                continue
            new_g = g_cost[current] + cost
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_val = new_g + heuristic(neighbor, goal)
                counter += 1
                heapq.heappush(open_set, (f_val, counter, neighbor))
                came_from[neighbor] = current

    if goal not in came_from:
        return None, None, None

    path = reconstruct_path(came_from, goal)
    return path, g_cost.get(goal, 0), expansion_order

st.set_page_config(page_title="Hospital Search Algorithms", layout="wide")
st.title("Emergency Supply Robot - Path Finding")
st.write("Find the optimal path through the hospital using GBFS or A*.")

nodes = list(hospital_graph.keys())

start = st.selectbox("Select Initial Node", nodes, index=nodes.index("Pharmacy"))
goal = st.selectbox("Select Goal Node", nodes, index=nodes.index("Emergency_Ward"))
algorithm = st.selectbox("Select Algorithm", ["GBFS", "A*"])

if st.button("Run Search"):
    if algorithm == "GBFS":
        path, cost, expansion_order = gbfs(start, goal)
    else:
        path, cost, expansion_order = a_star(start, goal)

    if path is None:
        st.error("No path found.")
    else:
        st.subheader("Search Result")
        st.write(f"**Algorithm:** {algorithm}")
        st.write(f"**Expansion Order:** {' → '.join(expansion_order)}")
        st.write(f"**Solution Path:** {' → '.join(path)}")
        st.write(f"**Total Path Cost:** {cost:.2f}")

        G = nx.DiGraph()
        for node, neighbors in hospital_graph.items():
            for neighbor, weight in neighbors.items():
                G.add_edge(node, neighbor, weight=weight)

        pos = locations
        path_edges = list(zip(path, path[1:]))
        node_colors = ["orange" if n in path else "lightblue" for n in G.nodes()]
        edge_colors = ["red" if e in path_edges else "gray" for e in G.edges()]

        fig, ax = plt.subplots(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors,
                node_size=2000, font_size=9, arrows=True, ax=ax)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels, ax=ax)
        ax.set_title(f"{algorithm} Solution Path")
        ax.axis("off")
        st.pyplot(fig)

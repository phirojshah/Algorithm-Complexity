import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

def is_clique(graph, subset):
    """
    Check if a given subset of nodes forms a complete subgraph (clique).
    """
    for u, v in combinations(subset, 2):
        if graph[u][v] == 0:
            return False
    return True

def find_largest_complete_subgraph(graph):
    """
    Find the largest complete subgraph (clique) in the graph.
    """
    n = len(graph)
    largest_clique = []

    # Check subsets of size k from n down to 2
    for k in range(n, 1, -1):  # Start with the largest possible subset size
        for subset in combinations(range(n), k):
            if is_clique(graph, subset):
                largest_clique = list(subset)  # Store the largest clique found
                return largest_clique  # Return the first largest clique found
    
    return largest_clique  # If no clique found, return an empty list

# Example graph (adjacency matrix)
graph = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 0]
]

# Create the graph using networkx
G = nx.Graph()
num_nodes = len(graph)

# Add nodes and edges to the graph
for i in range(num_nodes):
    G.add_node(i)

for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if graph[i][j] == 1:
            G.add_edge(i, j)

# Find the largest complete subgraph (clique)
clique = find_largest_complete_subgraph(graph)

# Plot the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Positioning for nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold', edge_color='gray')

# Highlight the clique nodes
if clique:
    clique_edges = [(clique[i], clique[j]) for i, j in combinations(clique, 2)]
    nx.draw_networkx_nodes(G, pos, nodelist=clique, node_color='orange')  # Highlight the clique nodes
    nx.draw_networkx_edges(G, pos, edgelist=clique_edges, edge_color='red', width=2)  # Highlight the clique edges

# Display the graph
plt.title("Graph with Largest Clique Highlighted")
plt.show()

# Output the largest clique in the terminal
if clique:
    print(f"Largest complete subgraph (clique) found: Nodes {clique}")
else:
    print("No complete subgraph found.")

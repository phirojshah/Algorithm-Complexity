import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq

# Create a random graph with 10 nodes
def generate_random_graph(num_nodes):
    G = nx.Graph()
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, 10)  # Random weight between 1 and 10
            edge = random.randint(0,2)
            if(edge == 1):
                G.add_edge(i, j, weight=weight)
    return G

# Prim's Algorithm to find MST
def prims_algorithm(graph, start):
    mst_edges = []  # To store the MST edges
    visited = set()  # To track visited vertices
    min_heap = [(0, start)]  # Priority queue (edge_weight, vertex)
    
    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        
        if vertex not in visited:
            visited.add(vertex)
            if weight > 0:  # Skip the initial 0 weight
                mst_edges.append((last_vertex, vertex, weight))
            
            # Add adjacent vertices and their weights
            for neighbor, data in graph[vertex].items():
                edge_weight = data['weight']
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
            last_vertex = vertex  # Update last vertex visited
    
    return mst_edges

# Generate a random graph with 10 nodes
G = generate_random_graph(10)

# Apply Prim's Algorithm
mst_prim = prims_algorithm(G, 0)

# Create a layout for visualization
pos = nx.spring_layout(G)

# Plot the original graph
plt.figure(figsize=(12, 8))

# Plot the original graph
plt.subplot(121)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=12, font_weight="bold", edge_color="gray")
plt.title("Original Graph")

# Plot MST from Prim's algorithm
plt.subplot(122)
edges_prim = [(u, v) for u, v, _ in mst_prim]
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=12, font_weight="bold", edge_color="green", width=2, edgelist=edges_prim)
plt.title("MST (Prim's Algorithm)")

plt.tight_layout()
plt.show()

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
            edge = random.randint(0,3)
            if(edge == 1):
                G.add_edge(i, j, weight=weight)
    return G

# Prim's Algorithm to find MST
def prims_algorithm(graph, start):
    mst_edges = []  # To store the MST edges
    visited = set()  # To track visited vertices
    min_heap = [(0, start)]  # Priority queue (edge_weight, vertex)
    last_vertex = start  # To keep track of the last vertex
    
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

# Kruskal's Algorithm to find MST
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal_algorithm(vertices, edges):
    mst = []  # To store the MST edges
    dsu = DisjointSet(vertices)
    
    # Sort edges based on their weight
    edges.sort(key=lambda edge: edge[2])
    
    for u, v, weight in edges:
        if dsu.find(u) != dsu.find(v):  # If adding this edge doesn't form a cycle
            mst.append((u, v, weight))
            dsu.union(u, v)
    
    return mst

# Generate a random graph with 10 nodes
G = generate_random_graph(10)

# Apply Prim's Algorithm
mst_prim = prims_algorithm(G, 0)

# Apply Kruskal's Algorithm
edges = [(u, v, data['weight']) for u, v, data in G.edges(data=True)]
mst_kruskal = kruskal_algorithm(10, edges)

# Create a layout for visualization
pos = nx.spring_layout(G)

# Plot the original graph
plt.figure(figsize=(14, 8))

# Plot the original graph
plt.subplot(131)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=12, font_weight="bold", edge_color="gray")
plt.title("Original Graph")

# Plot MST from Prim's algorithm
plt.subplot(132)
edges_prim = [(u, v) for u, v, _ in mst_prim]
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=12, font_weight="bold", edge_color="green", width=2, edgelist=edges_prim)
plt.title("MST (Prim's Algorithm)")

# Plot MST from Kruskal's algorithm
plt.subplot(133)
edges_kruskal = [(u, v) for u, v, _ in mst_kruskal]
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=12, font_weight="bold", edge_color="red", width=2, edgelist=edges_kruskal)
plt.title("MST (Kruskal's Algorithm)")

plt.tight_layout()
plt.show()

import time
import random
import matplotlib.pyplot as plt
from heapq import heappop, heappush

# Kruskal's Algorithm
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)
    mst = []
    
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
    return mst

# Prim's Algorithm
def prim(vertices, edges):
    adj_list = {i: [] for i in range(vertices)}
    for u, v, weight in edges:
        adj_list[u].append((weight, v))
        adj_list[v].append((weight, u))
    
    mst = []
    visited = set()
    start_node = random.randint(0, vertices - 1)
    min_heap = [(0, start_node)]  # (weight, vertex)
    
    while len(visited) < vertices and min_heap:
        weight, u = heappop(min_heap)
        if u not in visited:
            visited.add(u)
            mst.append((u, weight))
            for next_weight, v in adj_list[u]:
                if v not in visited:
                    heappush(min_heap, (next_weight, v))
    
    return mst if len(visited) == vertices else []  # Ensure full MST is formed

# Generate a connected graph
def generate_connected_graph(size):
    edges = []
    for i in range(size - 1):
        edges.append((i, i + 1, random.randint(1, 100)))  # Ensure connectivity
    for _ in range(size):
        u, v = random.randint(0, size - 1), random.randint(0, size - 1)
        if u != v:
            edges.append((u, v, random.randint(1, 100)))
    return edges

# Measure time for different sizes
sizes = [10, 50, 100, 200, 500]
times = {"Kruskal": [], "Prim": []}

for size in sizes:
    edges = generate_connected_graph(size)
    
    # Kruskal's Algorithm
    start = time.time()
    kruskal(size, edges)
    end = time.time()
    times["Kruskal"].append(end - start)
    
    # Prim's Algorithm
    start = time.time()
    prim(size, edges)
    end = time.time()
    times["Prim"].append(end - start)

# Plot results
plt.figure(figsize=(10, 6))
for name, t in times.items():
    plt.plot(sizes, t, marker='o', label=name)
plt.xlabel("Number of Vertices")
plt.ylabel("Time (seconds)")
plt.title("Kruskal's vs Prim's Algorithm Performance")
plt.legend()
plt.grid()
plt.show()
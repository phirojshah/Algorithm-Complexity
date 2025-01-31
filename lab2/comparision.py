import time
import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Activity Selection Problem
def greedy_activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]
    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])
    return selected

def brute_force_activity_selection(activities):
    from itertools import combinations
    n = len(activities)
    best_set = []
    for i in range(1, n+1):
        for subset in combinations(activities, i):
            if all(subset[j][0] >= subset[j-1][1] for j in range(1, len(subset))):
                if len(subset) > len(best_set):
                    best_set = subset
    return best_set

# Prim's Algorithm
def prim_mst(graph):
    return nx.minimum_spanning_tree(graph, algorithm='prim')

# Kruskal's Algorithm
def kruskal_mst(graph):
    return nx.minimum_spanning_tree(graph, algorithm='kruskal')

# N-Queens Problem

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_backtracking(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_backtracking(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def n_queens_brute_force(n):
    from itertools import permutations
    solutions = []
    for perm in permutations(range(n)):
        if n == len(set(perm[i] + i for i in range(n))) == len(set(perm[i] - i for i in range(n))):
            solutions.append(perm)
    return solutions

# Performance Measurement and Graph Plotting
def measure_time():
    activity_sizes = [10, 20, 30]
    mst_sizes = [50, 100, 200]
    n_queens_sizes = [4, 6, 8]

    activity_greedy_times = []
    activity_brute_times = []
    prim_times = []
    kruskal_times = []
    n_queens_backtracking_times = []
    n_queens_brute_times = []

    for size in activity_sizes:
        activities = [(random.randint(1, 50), random.randint(51, 100)) for _ in range(size)]
        start = time.time()
        greedy_activity_selection(activities)
        activity_greedy_times.append(time.time() - start)
        start = time.time()
        brute_force_activity_selection(activities)
        activity_brute_times.append(time.time() - start)

    for size in mst_sizes:
        graph = nx.gnm_random_graph(size, size * 2)
        for u, v in graph.edges():
            graph[u][v]['weight'] = random.randint(1, 100)
        start = time.time()
        prim_mst(graph)
        prim_times.append(time.time() - start)
        start = time.time()
        kruskal_mst(graph)
        kruskal_times.append(time.time() - start)

    for size in n_queens_sizes:
        board = [[0] * size for _ in range(size)]
        start = time.time()
        solve_n_queens_backtracking(board, 0, size)
        n_queens_backtracking_times.append(time.time() - start)
        start = time.time()
        n_queens_brute_force(size)
        n_queens_brute_times.append(time.time() - start)

    plt.figure()
    plt.plot(activity_sizes, activity_greedy_times, label="Greedy")
    plt.plot(activity_sizes, activity_brute_times, label="Brute Force")
    plt.xlabel("Number of Activities")
    plt.ylabel("Execution Time (s)")
    plt.title("Activity Selection Problem")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(mst_sizes, prim_times, label="Prim's Algorithm")
    plt.plot(mst_sizes, kruskal_times, label="Kruskal's Algorithm")
    plt.xlabel("Graph Size (Vertices)")
    plt.ylabel("Execution Time (s)")
    plt.title("Minimum Spanning Tree Comparison")
    plt.legend()
    plt.show()

    plt.figure()
    plt.plot(n_queens_sizes, n_queens_backtracking_times, label="Backtracking")
    plt.plot(n_queens_sizes, n_queens_brute_times, label="Brute Force")
    plt.xlabel("N")
    plt.ylabel("Execution Time (s)")
    plt.title("N-Queens Problem")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    measure_time()


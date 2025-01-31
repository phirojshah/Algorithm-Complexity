import time
import itertools
import matplotlib.pyplot as plt

def is_valid(board, n):
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False
    return True

def solve_backtracking(board, row, n, solutions):
    # Recursive backtracking function to place queens
    if row == n:
        solutions.append(board[:]) # Found a solution
        return
    for col in range(n):
        if is_safe(board, row, col):  # Check if placing queen is safe
            board[row] = col
            solve_backtracking(board, row + 1, n, solutions)  # Place queen in next row
            board[row] = -1  # Backtrack

def is_safe(board, row, col):
    # Check if it's safe to place a queen in the specified position
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def time_for_each_queen_bt(n):
    # Measure the time for each queen placement in the backtracking approach
    times = []
    board = [-1] * n
    def track_time(row):
        start_time = time.time()
        solve_backtracking(board, row, n, [])
        end_time = time.time()
        times.append(end_time - start_time)
    
    for row in range(n):
        track_time(row)
    return times

def time_for_each_queen_bf(n):
    # Measure the time for each queen placement in the brute force approach
    times = []
    start_time = time.time()
    solutions = 0
    for perm in itertools.permutations(range(n)):
        if is_valid(perm, n):
            solutions += 1
            times.append(time.time() - start_time)  # Track time for valid placement
    return times

def brute_force_nqueens(n):
    # Brute force to solve the n-queens problem and measure the total time
    start_time = time.time()
    solutions = 0
    for perm in itertools.permutations(range(n)):
        if is_valid(perm, n):
            solutions += 1
    end_time = time.time()
    return solutions, end_time - start_time

# Call backtracking and brute force time functions
n = 8
bf_times = time_for_each_queen_bf(n)  # Time for brute force
bt_times = time_for_each_queen_bt(n)  # Time for backtracking
solutions_bf, time_bf = brute_force_nqueens(n)

# Ensure both time lists are the same length by trimming excess data if needed
min_len = min(len(bf_times), len(bt_times), n)
bf_times = bf_times[:min_len]
bt_times = bt_times[:min_len]

# Plot the time for each queen placement for both approaches
plt.plot(range(1, min_len+1), bf_times, label='Brute Force')
plt.plot(range(1, min_len+1), bt_times, label='Backtracking')
plt.xlabel('Queen Placement')
plt.ylabel('Time (seconds)')
plt.title(f"Time for Each Queen Placement (Brute Force vs Backtracking) for {n} Queens")
plt.legend()
plt.show()
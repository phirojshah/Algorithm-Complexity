import itertools
import time
import matplotlib.pyplot as plt

# Function to check if the position is valid for placing a queen (Backtracking)
def is_valid_backtracking(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Backtracking function to solve N-Queens problem
def solve_n_queens_backtracking(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_valid_backtracking(board, row, col, n):
            board[row] = col
            if solve_n_queens_backtracking(board, row + 1, n):
                return True
            board[row] = -1
    return False

# Backtracking method to find the solution and time it
def backtracking_n_queens(n):
    board = [-1] * n
    start_time = time.time()
    if solve_n_queens_backtracking(board, 0, n):
        end_time = time.time()
        return end_time - start_time
    return end_time - start_time

# Brute force function to check if the board is valid
def is_valid_brute_force(board, n):
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j) or board[i] == board[j]:
                return False
    return True

# Brute force method to find the solution and time it
def brute_force_n_queens(n):
    columns = list(range(n))
    all_permutations = itertools.permutations(columns)
    
    start_time = time.time()
    for perm in all_permutations:
        if is_valid_brute_force(perm, n):
            end_time = time.time()
            return end_time - start_time
    return end_time - start_time

# Main function to solve N-Queens problem for a range of N and plot the time consumed
def solve_and_plot():
    backtracking_times = []
    brute_force_times = []
    n_values = list(range(4, 15))  # N values from 4 to 10
    
    for n in n_values:
        print(f"Solving for N={n}...")
        # Measure time for backtracking
        backtracking_time = backtracking_n_queens(n)
        backtracking_times.append(backtracking_time)
        
        # Measure time for brute force
        brute_force_time = brute_force_n_queens(n)
        brute_force_times.append(brute_force_time)
    
    # Plotting the times for both algorithms
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, backtracking_times, label='Backtracking', marker='o')
    plt.plot(n_values, brute_force_times, label='Brute Force', marker='o')
    
    plt.title('Time Comparison between Backtracking and Brute Force for N-Queens Problem')
    plt.xlabel('N (Board Size)')
    plt.ylabel('Time (Seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Solve and plot for N=4 to N=10
solve_and_plot()

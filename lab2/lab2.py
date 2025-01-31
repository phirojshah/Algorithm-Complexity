
# Backtracking.py
def is_safe(board, row, col, N):
    for i in range(col):  # Check row
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):  # Check upper diagonal
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):  # Check lower diagonal
        if board[i][j] == 1:
            return False
    return True

def solve_nq_backtrack(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nq_backtrack(board, col + 1, N):
                return True
            board[i][col] = 0  # Backtrack
    return False

# Nonbacktracking.py
def solve_nq_nonbacktrack(N):
    result = [0] * N
    def place_queen(col):
        if col == N:
            return True
        for row in range(N):
            if all(abs(row - result[c]) != col - c and row != result[c] for c in range(col)):
                result[col] = row
                if place_queen(col + 1):
                    return True
        return False
    return place_queen(0)

# time_n-queen.py
import time
import matplotlib.pyplot as plt

def measure_time(algorithm, N_values):
    times = []
    for N in N_values:
        start = time.perf_counter()
        algorithm(N)  # For N-Queens
        times.append(time.perf_counter() - start)
    return times

N_values = [4, 8, 12, 16]
bt_times = measure_time(lambda n: solve_nq_backtrack([[0]*n for _ in range(n)], 0, n), N_values)
nbt_times = measure_time(solve_nq_nonbacktrack, N_values)

plt.plot(N_values, bt_times, marker='o', label='Backtracking')
plt.plot(N_values, nbt_times, marker='s', label='Non-backtracking')
plt.xlabel('N (Board Size)')
plt.ylabel('Time (seconds)')
plt.title('N-Queens: Backtracking vs. Non-backtracking')
plt.legend()
plt.grid(True)
plt.show()

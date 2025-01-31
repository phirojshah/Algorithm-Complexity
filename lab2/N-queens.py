import matplotlib.pyplot as plt
import numpy as np

# Function to check if the position is valid for placing a queen
def is_valid(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Backtracking function to solve N-Queens problem
def solve_n_queens(board, row, n):
    # If all queens are placed
    if row == n:
        return True
    
    # Try placing queens in all columns for the current row
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row] = col  # Place the queen
            if solve_n_queens(board, row + 1, n):  # Recur to place the rest of the queens
                return True
            board[row] = -1  # Backtrack if placing queen does not work
    return False

# Function to visualize the chessboard
def visualize_solution(board, n):
    # Create an empty chessboard with alternating black and white squares
    chessboard = np.zeros((n, n))
    
    # Create a grid with alternating black and white squares
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                chessboard[i][j] = 1  # Mark black squares
    
    # Plot the chessboard
    plt.figure(figsize=(6, 6))
    plt.imshow(chessboard, cmap='binary', interpolation='none')

    # Place queens on the board (marking them with 'Q')
    for row in range(n):
        col = board[row]
        plt.text(col, row, 'Q', ha='center', va='center', color='red', fontsize=20, fontweight='bold')

    # Annotate grid lines and labels for rows and columns
    plt.xticks(range(n))
    plt.yticks(range(n))
    plt.gca().invert_yaxis()  # Invert Y-axis to match chessboard orientation
    plt.grid(True, which='both', color='black', linewidth=0)

    # Show the final title and the board
    plt.title(f'N-Queens Solution for N={n}')
    plt.show()

# Main function to solve the N-Queens problem and visualize
def n_queens_solution(n):
    board = [-1] * n  # Create an empty board
    if solve_n_queens(board, 0, n):
        print(f"Solution for N={n} found!")
        visualize_solution(board, n)
    else:
        print(f"No solution exists for N={n}.")

# Example: Solve and visualize for N=8 (Standard chessboard)
n_queens_solution(8)

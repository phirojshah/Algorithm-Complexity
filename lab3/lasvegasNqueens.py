import random
import tkinter as tk
from tkinter import ttk


class NQueensLasVegas:
    def __init__(self, n):
        self.n = n
        self.solution = None
        self.find_solution()
        self.display_solution()

    def is_safe(self, board, row, col):
        # Check previous rows for conflicts
        for i in range(row):
            if (
                board[i] == col or  # Same column
                board[i] - i == col - row or  # Same diagonal
                board[i] + i == col + row  # Same anti-diagonal
            ):
                return False
        return True

    def find_solution(self):
        """Find a solution to the N-Queens problem using the Las Vegas approach."""
        while True:
            board = [-1] * self.n  # Initialize the board
            available_columns = list(range(self.n))

            for row in range(self.n):
                # Randomly shuffle available columns
                random.shuffle(available_columns)
                placed = False
                for col in available_columns:
                    if self.is_safe(board, row, col):
                        board[row] = col
                        placed = True
                        break
                if not placed:
                    break  # Restart the process if placement fails
            else:
                self.solution = board
                return

    def draw_board(self, canvas, solution, tile_size):
        """Draw a chessboard with the given solution."""
        for i in range(self.n):
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "black"
                canvas.create_rectangle(
                    j * tile_size,
                    i * tile_size,
                    (j + 1) * tile_size,
                    (i + 1) * tile_size,
                    fill=color,
                )
        # Place queens
        for row, col in enumerate(solution):
            x_center = col * tile_size + tile_size // 2
            y_center = row * tile_size + tile_size // 2
            radius = tile_size // 4
            canvas.create_oval(
                x_center - radius,
                y_center - radius,
                x_center + radius,
                y_center + radius,
                fill="red",
            )

    def display_solution(self):
        """Display the solution using Tkinter."""
        if not self.solution:
            print("No solution found.")
            return

        root = tk.Tk()
        root.title(f"{self.n}-Queens Las Vegas Solution")

        # Create a canvas
        tile_size = 85
        board_size = self.n * tile_size
        canvas = tk.Canvas(root, width=board_size, height=board_size, bg="white")
        canvas.pack()

        # Draw the solution
        self.draw_board(canvas, self.solution, tile_size)

        # Add label to display the solution
        label = ttk.Label(root, text=f"Solution: {self.solution}", anchor="center")
        label.pack()

        root.mainloop()


# Run the Las Vegas N-Queens Visualizer
if __name__ == "__main__":
    N = 8  # Change this value for different board sizes
    NQueensLasVegas(N)
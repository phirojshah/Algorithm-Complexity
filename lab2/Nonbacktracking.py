import random

global N
global COUNT
N = 8

global Q
Q = 0

def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def isSafe(board, row, col):
    # Check this row on left and right sides
    for i in range(N):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on right side
    for i, j in zip(range(row, N, 1), range(col, N, 1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    global COUNT
    COUNT = COUNT + 1
    global Q

    # Base case: If all queens are placed then return true
    if Q == 8:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
            Q += 1

            # Recur to place the rest of the queens
            if solveNQUtil(board, (col + 1) % 8) == True:
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, remove queen
            board[i][col] = 0
            Q -= 1

    return False

def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if solveNQUtil(board, random.randint(0, 7)) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

# Driver Code
if __name__ == '__main__':
    COUNT = 0
    solveNQ()
    print("The total number of positions it took using non-backtracking algorithm = " + str(COUNT))

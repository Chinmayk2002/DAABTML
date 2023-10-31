# Design n-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final 8-queen‟s matrix.

def is_safe(board, row, col):
    # Check if there's a Queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there's a Queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there's a Queen in the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                return True

            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))

if __name__ == "__main__":
    n = 4
    board = [[0] * n for _ in range(n)]

    # Place the first Queen
    board[0][1] = 1

    if solve_n_queens(board, 1):
        print("4-Queens Solution:")
        print_board(board)
    else:
        print("No solution found.")

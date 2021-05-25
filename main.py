# Sudoku Solver
import time

if __name__ == '__main__':
    # EASY
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    # MEDIUM
    """
    board = [
        [7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 9, 0, 0, 3, 0, 0, 0, 8],
        [6, 0, 8, 0, 0, 5, 0, 7, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 2],
        [0, 0, 2, 1, 0, 0, 0, 0, 6],
        [0, 0, 3, 0, 0, 2, 0, 0, 0],
        [0, 5, 0, 0, 0, 3, 7, 0, 0],
        [0, 1, 0, 0, 9, 0, 4, 0, 0]
    ]
    """

    # HARD
    """
    board = [
        [0, 0, 5, 3, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 7, 0, 0, 1, 0, 5, 0, 0],
        [4, 0, 0, 0, 0, 5, 3, 0, 0],
        [0, 1, 0, 0, 7, 0, 0, 0, 6],
        [0, 0, 3, 2, 0, 0, 0, 8, 0],
        [0, 6, 0, 5, 0, 0, 0, 0, 9],
        [0, 0, 4, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 9, 7, 0, 0]
    ]
    """

    # EXPERT
    """
    board = [
        [1, 0, 0, 0, 0, 7, 0, 9, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 8],
        [0, 0, 9, 6, 0, 0, 5, 0, 0],
        [0, 0, 5, 3, 0, 0, 9, 0, 0],
        [0, 1, 0, 0, 8, 0, 0, 0, 2],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 3, 0, 0]
    ]
    """


# Printing the board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print('- - - - - - - - - - - - ')

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')


def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # Check values
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            # If valid, put it in the board.
            board[row][col] = i

            # Solved?
            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


# Checking if the board is valid
def valid(board, number, position):
    # Check rows
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check columns
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Check 3x3 boxes
    box_x = position[1] // 3
    box_y = position[0] // 3

    # Loop through boxes, check for duplicate elements
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    return True


# Find empty squares
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, col



def solve():
    start = time.time()
    print(f'{print_board(board)}')
    solve_sudoku(board)
    print(f'{print_board(board)}')
    end = time.time()
    print(f'Solved in {end - start} second(s).')


solve()

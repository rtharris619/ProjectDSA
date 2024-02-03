board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve_puzzle(bo):
    cell = find_empty_cell(bo)
    if cell is None:
        return True

    row, col = cell

    for num in range(1, 10):
        if is_number_valid_in_cell(bo, num, (row, col)):
            bo[row][col] = num

            if solve_puzzle(bo):
                return True

            bo[row][col] = 0

    return False


def find_empty_cell(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return row, col
    return None


def is_number_valid_in_cell(bo, num, cell):

    # check row
    for col in range(len(bo[0])):
        if num == bo[cell[0]][col] and col != cell[1]:
            return False

    # check column
    for row in range(len(bo)):
        if num == bo[row][cell[1]] and row != cell[0]:
            return False

    # check box
    start_row = cell[0] // 3 * 3
    end_row = start_row + 3

    start_col = cell[1] // 3 * 3
    end_col = start_col + 3

    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            if num == bo[row][col] and (row, col) != cell:
                return False

    return True


def print_board(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if col == 0:
                print(" ", end="")
            print(bo[row][col], end=" ")

            if (col + 1) % 3 == 0 and col != len(bo[0]) - 1:
                print("|", end=" ")

        print("")

        if (row + 1) % 3 == 0:
            print("-----------------------")


def solve():
    print_board(board)
    solve_puzzle(board)
    print(" ")
    print_board(board)

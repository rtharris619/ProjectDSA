import queue
from typing import Tuple, List


def create_maze():
    maze = [["#", "#", "#", "#", "#", " ", "#", "#", "#"],
            ["#", " ", "S", " ", " ", " ", " ", " ", "#"],
            ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
            ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
            ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
            ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
            ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
            ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "E", "#"]]

    return maze


def get_start(maze):
    start_x = start_y = -1

    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if maze[i][j] == "S":
                start_x = i
                start_y = j

    return start_x, start_y


def is_valid(maze: List[List[str]], start_pos: Tuple[int, int], moves: str):

    row = start_pos[0]
    col = start_pos[1]

    for move in moves:
        if move == "U":
            row -= 1
        if move == "D":
            row += 1
        if move == "R":
            col += 1
        if move == "L":
            col -= 1

        if row < 0 or row >= len(maze):
            return False

        if col < 0 or col >= len(maze[0]):
            return False

        if maze[row][col] == "#":
            return False

    return True


def find_end(maze: List[List[str]], start_pos: Tuple[int, int], moves: str):
    row = start_pos[0]
    col = start_pos[1]

    for move in moves:
        if move == "U":
            row -= 1
        if move == "D":
            row += 1
        if move == "R":
            col += 1
        if move == "L":
            col -= 1

        if maze[row][col] == "E":
            print("Moves:", moves)
            return True

    return False


def solve():
    paths = queue.Queue()
    paths.put("")
    path = ""
    maze = create_maze()

    start_pos = get_start(maze)

    while not find_end(maze, start_pos, path):
        path = paths.get()
        for i in ["U", "R", "D", "L"]:
            moves = path + i
            if is_valid(maze, start_pos, moves):
                paths.put(moves)


def driver():
    solve()

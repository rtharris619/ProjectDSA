import queue
from typing import List, Tuple


def create_maze():
    maze = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "F", "X", ".", ".", ".", ".", ".", "."],
            [".", "|", ".", ".", ".", ".", ".", ".", "."],
            [".", "|", ".", ".", ".", ".", ".", ".", "."],
            [".", "L", "-", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]

    return maze


def init_visited(maze: List[List[str]]):
    visited = [[False for _ in enumerate(maze)] for _ in enumerate(maze)]
    return visited


def get_start(maze: List[List[str]]):
    start_x = start_y = -1

    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if maze[i][j] == "X":
                start_x = i
                start_y = j

    return start_x, start_y


def is_valid(maze: List[List[str]], start_pos: Tuple[int, int], moves: str, visited: List[List[bool]]):

    row = start_pos[0]
    col = start_pos[1]

    for move in moves:
        if move == "N":
            row -= 1
        if move == "S":
            row += 1
        if move == "E":
            col += 1
        if move == "W":
            col -= 1

        if row < 0 or row >= len(maze):
            return False

        if col < 0 or col >= len(maze[0]):
            return False

        if maze[row][col] == ".":
            return False

        if move == "N":
            if maze[row][col] == "L" or maze[row][col] == "J":
                return False

        if move == "S":
            if maze[row][col] == "F" or maze[row][col] == "7":
                return False

        if move == "E":
            if maze[row][col] == "L" or maze[row][col] == "F":
                return False

        if move == "W":
            if maze[row][col] == "7" or maze[row][col] == "J":
                return False

        visited[row][col] = True

    return True


def find_end(maze: List[List[str]], start_pos: Tuple[int, int], moves: str):
    row = start_pos[0]
    col = start_pos[1]

    for move in moves:
        if move == "N":
            row -= 1
        if move == "S":
            row += 1
        if move == "E":
            col += 1
        if move == "W":
            col -= 1

        if maze[row][col] == "-":
            print("Moves:", moves)
            return True

    return False


def solve():
    paths = queue.Queue()
    paths.put("")
    path = ""
    maze = create_maze()
    visited = init_visited(maze)

    start_pos = get_start(maze)

    counter = 0

    while not find_end(maze, start_pos, path):
        path = paths.get()
        for i in ["N", "S", "E", "W"]:
            moves = path + i
            if is_valid(maze, start_pos, moves, visited):
                paths.put(moves)
        counter += 1

    # print(visited)
    print("end")


def driver():
    solve()

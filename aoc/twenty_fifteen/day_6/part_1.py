from pathlib import Path
from aoc.helpers.input import Input

# Bonus challenge:
# For this puzzle, I'd use the 2D list first.
# If you're interested in optimization, a bytearray is a more promising alternative than a set.

def solve(instructions: list[str]):
    n = 1000
    grid = [[0] * n for _ in range(n)]

    for instruction in instructions:
        process_input_line(instruction, grid)

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count += grid[row][col]
    return count

def process_input_line(instruction: str, grid: list[list[int]]):
    turn_on = "turn on"
    turn_off = "turn off"
    toggle = "toggle"
    if instruction.startswith(turn_on):
        turn_on_lights(instruction, grid)
    if instruction.startswith(turn_off):
        turn_off_lights(instruction, grid)
    if instruction.startswith(toggle):
        toggle_lights(instruction, grid)

def turn_on_lights(instruction: str, grid: list[list[int]]):
    split = instruction.split()
    x1, y1 = [int(item) for item in split[2].split(",")]
    x2, y2 = [int(item) for item in split[4].split(",")]
    for row in range(y1, y2 + 1):
        for col in range(x1, x2 + 1):
            grid[row][col] = 1

def turn_off_lights(instruction: str, grid: list[list[int]]):
    split = instruction.split()
    x1, y1 = [int(item) for item in split[2].split(",")]
    x2, y2 = [int(item) for item in split[4].split(",")]
    for row in range(y1, y2 + 1):
        for col in range(x1, x2 + 1):
            grid[row][col] = 0

def toggle_lights(instruction: str, grid: list[list[int]]):
    split = instruction.split()
    x1, y1 = [int(item) for item in split[1].split(",")]
    x2, y2 = [int(item) for item in split[3].split(",")]
    for row in range(y1, y2 + 1):
        for col in range(x1, x2 + 1):
            if grid[row][col] == 0:
                grid[row][col] = 1
            else:
                grid[row][col] = 0

def tests():
    instructions = ["toggle 0,0 through 999,0"]
    res = solve(instructions)
    print(res) # 1 million lights


def solution():
    input = Input(Path(__file__).resolve().parent).extract_by_newline()
    res = solve(input)
    print(res)


def driver():
    solution()

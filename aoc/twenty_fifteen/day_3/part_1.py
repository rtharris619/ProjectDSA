from pathlib import Path
from aoc.helpers.input import Input

def solve(input: str):
    north = '^'
    south = 'v'
    east =  '>'
    west =  '<'
    current_x, current_y = (0, 0)
    grid = set([(current_x, current_y)])
    for char in input:
        if char == north:
            current_y += 1
        if char == south:
            current_y -= 1
        if char == east:
            current_x += 1
        if char == west:
            current_x -= 1
        if (current_x, current_y) not in grid:
            grid.add((current_x, current_y))
    return len(grid)

def tests():
    input = ">"
    res = solve(input)
    print(res)
    input = "^>v<"
    res = solve(input)
    print(res)
    input = "^v^v^v^v^v"
    res = solve(input)
    print(res)

def solution():
    input = Input(Path(__file__).resolve().parent).extract()    
    res = solve(input)
    print(res)

def driver():
    solution()

from pathlib import Path
from aoc.helpers.input import Input

def get_next_position(current: tuple[int, int], char: str):
    north = '^'
    south = 'v'
    east =  '>'
    west =  '<'
    current_x, current_y = current

    if char == north:
        current_y += 1
    if char == south:
        current_y -= 1
    if char == east:
        current_x += 1
    if char == west:
        current_x -= 1

    return (current_x, current_y)

def solve(input: str):
    santas_turn = True
    santas_pos = (0, 0)
    robo_santas_pos = (0, 0)    
    grid = set([santas_pos])
    
    for char in input:
        if santas_turn:
            santas_pos = get_next_position(santas_pos, char)
            if santas_pos not in grid:
                grid.add(santas_pos)
        else:
            robo_santas_pos = get_next_position(robo_santas_pos, char)
            if robo_santas_pos not in grid:
                grid.add(robo_santas_pos)
        santas_turn = not santas_turn
    
    return len(grid)

def tests():
    input = "^v"
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

from pathlib import Path
from aoc.helpers.input import Input

def solve(input: str):
    floor = 0
    basement = -1
    for position, char in enumerate(input, 1):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == basement:
            return position

def tests():
    input = '()())'
    res = solve(input)
    print(res)

def solution():
    input = Input(Path(__file__).resolve().parent).extract()
    res = solve(input)
    print(res)

def driver():
    solution()

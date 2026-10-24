from pathlib import Path
from aoc.helpers.input import Input

def solve(input: str):
    floor = 0
    for char in input:
        if char == '(':
            floor+=1
        else:
            floor-=1
    return floor

def tests():
    input = '(()(()('
    res = solve(input)
    print(res)

def solution():
    input = Input(Path(__file__).resolve().parent).extract()
    res = solve(input)
    print(res)

def driver():
    solution()

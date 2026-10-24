from pathlib import Path
from aoc.helpers.input import Input

def solve(input: list[str]):
    total_square_feet = 0

    for item in input:
        l, w, h = [int(x) for x in item.split('x')]
        area_1 = l * w
        area_2 = w * h
        area_3 = h * l
        surface_area = 2 * (area_1 + area_2 + area_3)

        extra_paper = min(area_1, area_2, area_3)
        total_square_feet += (surface_area + extra_paper)

    return total_square_feet

def tests():
    input = '2x3x4'
    res = solve([input])
    print(res)

    input = '1x1x10'
    res = solve([input])
    print(res)

def solution():
    input = Input(Path(__file__).resolve().parent).extract_by_newline()
    res = solve(input)
    print(res)

def driver():
    solution()

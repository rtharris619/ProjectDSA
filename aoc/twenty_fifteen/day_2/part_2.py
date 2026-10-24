from pathlib import Path
from aoc.helpers.input import Input

def solve(input: list[str]):
    total_feat_of_ribbon = 0

    for item in input:
        l, w, h = [int(x) for x in item.split('x')]
        top_and_bottom = (2 * l) + (2 * w)
        front_and_back = (2 * l) + (2 * h)
        left_and_right = (2 * w) + (2 * h)
        present_ribbon = min(top_and_bottom, front_and_back, left_and_right)
        bow_ribbon = l * w * h
        total_feat_of_ribbon += present_ribbon + bow_ribbon

    return total_feat_of_ribbon

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

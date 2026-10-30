from pathlib import Path
from aoc.helpers.input import Input


def solve(input: str):
    pass


def tests():
    input = "abc"
    res = solve(input)
    print(res)


def solution():
    input = Input(Path(__file__).resolve().parent).extract_by_newline()
    res = solve(input)
    print(res)


def driver():
    tests()
    solution()

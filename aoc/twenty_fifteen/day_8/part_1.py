from pathlib import Path
from aoc.helpers.input import Input
import ast


def solve(input: list[str]):
    string_data = 0
    code_data = 0
    for line in input:
        string_data += len(line)
        code_data += len(ast.literal_eval(line))
    return string_data - code_data


def tests():
    input = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
    res = solve(input)
    print(res)


def solution():
    input = Input(Path(__file__).resolve().parent).extract_by_newline()
    res = solve(input)
    print(res)


def driver():
    # tests()
    solution()

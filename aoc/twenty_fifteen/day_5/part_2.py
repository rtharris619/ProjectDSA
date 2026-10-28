from pathlib import Path
from aoc.helpers.input import Input

def solve(input: list[str]):
    nice_strings = 0
    
    for string in input:
        if is_nice(string):
            nice_strings += 1

    return nice_strings

def is_nice(string: str):
    pairs = {}
    pair_match = False
    repeating_match = False

    for i in range(len(string) - 1):
        eval = string[i: i + 2]
        if eval in pairs:
            # check for non-overlapping chars
            if i > pairs[eval] + 1:
                pair_match = True
                break
        else:
            pairs[eval] = i

    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            repeating_match = True
            break

    return pair_match and repeating_match

def tests():
    input = ["qjhvhtzxzqqjkmpb"]
    res = solve(input)
    print(res) # true

    input = ["xxyxx"]
    res = solve(input)
    print(res) # true

    input = ["uurcxstgmygtbstg"]
    res = solve(input)
    print(res) # false

    input = ["ieodomkazucvgmuy"]
    res = solve(input)
    print(res) # false

def solution():
    input = Input(Path(__file__).resolve().parent).extract_by_newline()
    res = solve(input)
    print(res)

def driver():
    solution()

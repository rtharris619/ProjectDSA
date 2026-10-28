from pathlib import Path
from aoc.helpers.input import Input

def solve(input: list[str]):
    nice_strings = 0

    for item in input:
        if is_nice(item):
            nice_strings += 1

    return nice_strings

def is_nice(string: str):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    req_vowels = 3
    vowel_count = 0
    naughties = set(['ab', 'cd', 'pq', 'xy'])
    doubles = False

    for i in range(len(string) - 1):
        if string[i] in vowels or (i == len(string) - 2 and string[i + 1] in vowels):
            vowel_count += 1
        if string[i] == string[i + 1]:
            doubles = True
        if string[i] + string[i + 1] in naughties:
            return False

    return vowel_count >= req_vowels and doubles

def tests():
    input = ["ugknbfddgicrmopn"]
    res = solve(input)
    print(res) # true

    input = ["aaa"]
    res = solve(input)
    print(res) # true

    input = ["jchzalrnumimnmhp"]
    res = solve(input)
    print(res) # false

    input = ["haegwjzuvuyypxyu"]
    res = solve(input)
    print(res) # false

    input = ["dvszwmarrgswjxmb"]
    res = solve(input)
    print(res) # false

def solution():
    input = Input(Path(__file__).resolve().parent).extract_by_newline()
    res = solve(input)
    print(res)

def driver():
    solution()

from typing import List


def letter_combinations(digits: str) -> List[str]:
    result = []

    digit_to_char = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(i, cur_str):
        if len(cur_str) == len(digits):
            result.append(cur_str)
            return

        for c in digit_to_char[digits[i]]:
            backtrack(i + 1, cur_str + c)

    if digits:
        backtrack(0, "")

    return result


def solve():
    digits = "23"
    result = letter_combinations(digits)
    print(result)

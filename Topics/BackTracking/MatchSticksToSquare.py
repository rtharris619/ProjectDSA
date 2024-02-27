# LeetCode 473
from typing import List


def make_square(sticks: List[int]):
    s = sum(sticks)
    if s % 4 != 0:
        return False

    length = sum(sticks) // 4
    sides = [0] * 4

    # To eliminate sticks first with length larger than what's possible
    sticks.sort(reverse=True)

    def backtrack(i: int):
        if i == len(sticks):
            return True

        for j in range(4):
            if sides[j] + sticks[i] <= length:
                sides[j] += sticks[i]
                if backtrack(i + 1):
                    return True
                sides[j] -= sticks[i]
        return False

    return backtrack(0)


def solve():
    match_sticks = [1, 1, 2, 2, 2]
    result = make_square(match_sticks)
    print(result)

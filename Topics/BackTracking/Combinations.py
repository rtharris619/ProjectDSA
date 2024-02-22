from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    result = []

    def backtrack(start: int, combination: List[int]):
        if len(combination) == k:
            result.append(combination[:])
            return

        for i in range(start, n + 1):
            combination.append(i)
            backtrack(i + 1, combination)
            combination.pop()

    backtrack(1, [])

    return result


def solve():
    n = 4
    k = 2

    result = combine(n, k)
    print(result)

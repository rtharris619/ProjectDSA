from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    result = []

    def backtrack(current: List[int], pos: int, tgt: int):
        if tgt == 0:
            result.append(current[:])
        if tgt <= 0:
            return

        previous = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == previous:
                continue
            current.append(candidates[i])
            backtrack(current, i + 1, tgt - candidates[i])
            current.pop()
            previous = candidates[i]

    backtrack([], 0, target)

    return result


def solve():
    candidates = [10, 1, 2, 7, 6, 1]
    target = 8

    result = combination_sum(candidates, target)
    print(result)

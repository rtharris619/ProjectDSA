from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(i, current, total):
        if target == total:
            result.append(current[:])
            return
        if i >= len(candidates) or total > target:
            return

        current.append(candidates[i])
        dfs(i, current, total + candidates[i]) # left branch
        current.pop()
        dfs(i + 1, current, total) # right branch

    dfs(0, [], 0)
    return result


def solve():
    candidates = [2, 3, 6, 7]
    target = 7
    result = combination_sum(candidates, target)
    print(result)

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)

    return result


def solve():
    nums = list(range(1, 4))
    result = permute(nums)
    print(result)

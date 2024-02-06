from typing import List


def permute_unique(nums: List[int]) -> List[List[int]]:
    result = []
    perm = []
    count = {n: 0 for n in nums}
    for n in nums:
        count[n] += 1

    def dfs():
        if len(perm) == len(nums):
            result.append(perm[:])
            return

        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] -= 1

                dfs()

                count[n] += 1
                perm.pop()

    dfs()
    return result


def solve():
    nums = [1, 1, 2]
    result = permute_unique(nums)
    print(result)

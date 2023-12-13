###
# 1: Two Sum
###

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, val in enumerate(nums):

            if target - val in visited.values():
                key = [k for k, v in visited.items() if v == target - val][0]
                return [key, i]

            visited[i] = val

        return []

    def twoSumImproved(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, val in enumerate(nums):

            if target - val in visited:
                return [visited[target - val], i]

            visited[val] = i


def test1():
    nums = [2, 7, 11, 15]
    target = 9
    return nums, target


def test2():
    nums = [3, 2, 4]
    target = 6

    return nums, target


def solve():
    s = Solution()

    nums, target = test2()

    result = s.twoSumImproved(nums, target)
    print(result)

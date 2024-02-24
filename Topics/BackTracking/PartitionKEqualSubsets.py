# LeetCode 698

from typing import List


def can_partition_k_subsets(nums: List[int], k: int) -> bool:

    if sum(nums) % k:
        return False
    nums.sort(reverse=True)

    target = sum(nums) / k
    used = [False] * len(nums)

    def backtrack(i: int, partitions: int, subset_sum: int):
        if partitions == 0:
            return True
        if subset_sum == target:
            return backtrack(0, partitions - 1, 0)

        for j in range(i, len(nums)):
            if used[j] or subset_sum + nums[j] > target:
                continue
            used[j] = True
            if backtrack(j + 1, partitions, subset_sum + nums[j]):
                return True
            used[j] = False

        return False

    return backtrack(0, k, 0)


def solve():
    nums = [4,3,2,3,5,2,1]
    k = 4
    result = can_partition_k_subsets(nums, k)
    print(result)

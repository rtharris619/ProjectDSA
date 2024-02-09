from typing import List


def number_of_subsets(nums):
    return 2 ** len(nums)


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    subset = []

    def dfs(i):
        if i >= len(nums):
            result.append(subset[:])
            return
        # decision to include nums[i] -> Left branch of decision tree.
        subset.append(nums[i])
        dfs(i + 1)

        # decision NOT to include nums[i] -> Right branch of decision tree.
        subset.pop()
        dfs(i + 1)

    dfs(0)

    return result


def solve():
    nums = [1, 2, 3]
    nr = number_of_subsets(nums)
    print("Number of subsets: ", nr)

    result = subsets(nums)
    print(result)

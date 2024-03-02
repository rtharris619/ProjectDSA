from typing import List


def binary_search(nums: List[int], target: int) -> bool:

    if len(nums) <= 0:
        return False

    midpoint = len(nums) // 2

    if target == nums[midpoint]:
        return True

    if target < nums[midpoint]:
        return binary_search(nums[0:midpoint-1], target)
    else:
        return binary_search(nums[midpoint+1:], target)


def binary_search_index(nums: List[int], target: int, left: int, right: int) -> int:

    if left > right:
        return -1

    midpoint = (left + right) // 2

    if target == nums[midpoint]:
        return midpoint

    if target < nums[midpoint]:
        return binary_search_index(nums, target, left, midpoint - 1)
    else:
        return binary_search_index(nums, target, midpoint + 1, right)


def test_1():
    nums = [1, 3, 5, 6, 7, 9, 12, 15, 17, 21, 23, 35]
    target = 21
    result = binary_search(nums, target)
    print(result)


def test_2():
    nums = [1, 3, 5, 6, 7, 9, 12, 15, 17, 21, 23, 35]
    target = 6
    result = binary_search_index(nums, target, 0, len(nums))
    print(result)


def driver():
    # test_1()
    test_2()

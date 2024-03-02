from typing import List


def quick_sort(nums: List[int], low: int, high: int):
    if low < high:

        pivot = partition(nums, low, high)

        # sort on the left of pivot
        quick_sort(nums, low, pivot - 1)
        # sort on the right of pivot
        quick_sort(nums, pivot + 1, high)


def partition(nums: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = nums[high]

    for j in range(low, high):
        if pivot >= nums[j]:
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]

    return i + 1


def test1():
    nums = [10, 80, 30, 90, 40, 50, 70]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)


def driver():
    test1()

# Write a function, merge_sort, that takes in a list of numbers as an argument. 
# The function should return a new list containing elements of the original list sorted in ascending order. 
# Your function must implement the merge sort algorithm.

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_side = merge_sort(nums[mid:])
    right_side = merge_sort(nums[:mid])

    return merge_2(left_side, right_side)

# Slow merge -> O(n*n + m*m)
def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged += left
    merged += right
    return merged

from collections import deque

# Fast merge -> O(n)
def merge_2(left, right):
    left = deque(left)
    right = deque(right)
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.popleft())
        else:
            merged.append(right.popleft())
    merged += left
    merged += right
    return merged

def driver():
    numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
    res = merge_sort(numbers) # -> [ 4, 5, 5, 6, 8, 10, 12, 40, 42, 100 ] 
    print(res)

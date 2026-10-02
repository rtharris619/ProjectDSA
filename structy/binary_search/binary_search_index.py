def binary_search_index(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid

    return left

def driver():
    res = binary_search_index([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> 8
    print(res)
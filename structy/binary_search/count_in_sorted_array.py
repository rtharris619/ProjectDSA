def find_left_most_index(nums, target):
    leftmost = -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            leftmost = mid
            right = mid - 1
    return leftmost

def find_right_most_index(nums, target):
    rightmost = -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            rightmost = mid
            left = mid + 1
    return rightmost

def count_in_sorted_array(nums, target):
    left = find_left_most_index(nums, target)
    right = find_right_most_index(nums, target)
    return 0 if left == -1 else right - left + 1

def driver():
    res = count_in_sorted_array([1,2,3,3,3,3,3,4,5,6,6,7,8,8,8,9], 3) # -> 5
    print(res)
    res = count_in_sorted_array([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 12) # -> 0
    print(res)
    res = count_in_sorted_array([42], 42) # -> 1
    print(res)
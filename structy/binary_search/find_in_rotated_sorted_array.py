def find_inflection_point(nums) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return left

def binary_search(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1

def find_in_rotated_sorted_array(nums, target):
    inflection_point = find_inflection_point(nums)
    left_result = binary_search(nums, target, 0, inflection_point - 1)
    right_result = binary_search(nums, target, inflection_point, len(nums) - 1)
    return left_result if left_result >= 0 else right_result

def driver():
    res = find_in_rotated_sorted_array([5,6,7,9,2,3,4], 7) # -> 2
    print(res) # the original array was [2,3,4,5,6,7,9] and was rotated 4 times
    res = find_in_rotated_sorted_array([15,22,37,42,59,70,3,8], 45) # -> -1
    print(res)
    res = find_in_rotated_sorted_array([5,6,7,8,10], 5) # -> 0
    print(res)
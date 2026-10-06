def min_in_rotated_sorted_array(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]

def driver():
    res = min_in_rotated_sorted_array([6,7,9,10,2,3,4,5]) # -> 2
    print(res) # the original array was [2,3,4,5,6,7,9,10] and was rotated 4 times

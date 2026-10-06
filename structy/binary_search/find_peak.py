def find_peak(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        elif nums[mid] > nums[mid + 1]:
            right = mid
    return left

def driver():
    res = find_peak([4,5,6,3,1]) # -> 2
    print(res) # 6 is a peak b/c it is greater than both of its neighbors 
    res = find_peak([2,5,7,10,12]) # -> 4
    print(res) # 12 is a peak b/c it is greater than its single neighbor

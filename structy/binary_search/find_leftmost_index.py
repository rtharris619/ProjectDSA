def find_leftmost_index(nums, target):
    leftmost = -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            leftmost = mid
            right = mid - 1

    return leftmost

def driver():
    res = find_leftmost_index([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 3) # -> 2
    print(res)
    res = find_leftmost_index([2,2,5,7,8,8,10,10,10,12,15,18,20], 10) # -> 6
    print(res)
    res = find_leftmost_index([1,2,3,3,3,4,5,6,6,7,8,8,8,9], 12) # -> -1
    print(res)
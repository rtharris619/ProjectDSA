def five_sort(nums):
    start = 0
    end = len(nums) - 1

    while start <= end:
        if nums[end] == 5:
            end -= 1
        elif nums[start] == 5:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
        else:
            start += 1
    return nums

def driver():
    res = five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5])
    print(res)
    # -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 

def find_subarray_sum(nums: list[int], target_sum: int) -> tuple[int, int]:
    start = 0
    window_sum = 0
    for end in range(0, len(nums)):
        window_sum += nums[end]
        while window_sum > target_sum:
            window_sum -= nums[start]
            start += 1
        if window_sum == target_sum:
            return (start, end)

def driver():
    res = find_subarray_sum([1, 2, 3, 7, 5], 12) # -> (1,3)
    print(res)
    # the subarray that spans indices 1 to 3 is [2,3,7] and its sum is 12

def longest_subarray_sum(nums: list[int], target_sum: int) -> int:
    longest = -1
    start = 0
    window_sum = 0
    for end in range(0, len(nums)):
        window_sum += nums[end]
        while window_sum > target_sum:
            window_sum -= nums[start]
            start += 1
        if window_sum == target_sum:
            current_length = end - start + 1
            if current_length > longest:
                longest = current_length

    return longest

def driver():
    res = longest_subarray_sum([1, 2, 1, 5, 2, 3, 10, 1, 9, 4, 3, 3, 7], 10) # -> 4
    print(res)
    # the longest subarray with a sum of 10 is [2, 1, 5, 2] and its length is 4
    
    res = longest_subarray_sum([2, 4, 1, 1, 2], 10) # -> 5
    print(res)
    res = longest_subarray_sum([10, 4, 8, 0, 4], 8) # -> 2
    print(res)
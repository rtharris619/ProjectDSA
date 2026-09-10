from math import inf

# naive solution
def max_subarray_sum_size_k(nums, k):
    max_sum = -inf
    for i in range(0, len(nums) - k + 1):
        current_sum = sum(nums[i: i + k])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# optimised solution
def max_subarray_sum_size_k_2(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(0, len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

def driver():
    res = max_subarray_sum_size_k_2([4, 2, 1, -9, 8, 4, 3], 3) # -> 15
    print(res)
    # [8,4,3] is the subarray of size 3 with the maximal sum

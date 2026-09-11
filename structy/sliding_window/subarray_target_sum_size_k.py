
def subarray_target_sum_size_k(nums, target, k):
    count = 0
    current_sum = sum(nums[0:k])
    if current_sum == target:
        count += 1
    for i in range(0, len(nums) - k):
        current_sum -= nums[i]
        current_sum += nums[i + k]
        if current_sum == target:
            count += 1
    return count

def driver():
    res = subarray_target_sum_size_k([2, 3, 2, 2, 3, 1, 3, 8, 5, 0, 2, 4], 7, 3) # -> 5
    print(res)
    # The 5 subarrays of size 3 whose sum is 7 are:
    #   [2,3,2]
    #   [3,2,2]
    #   [2,2,3]
    #   [3,1,3]
    #   [5,0,2]

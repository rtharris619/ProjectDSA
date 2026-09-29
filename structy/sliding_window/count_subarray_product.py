def count_subarray_product(nums, target_product):
    count = 0
    start = 0
    product = 1

    for end in range(len(nums)):
        product *= nums[end]
        while product >= target_product and start <= end:
            product /= nums[start]
            start += 1
        count += end - start + 1

    return count

def driver():
    res = count_subarray_product([2, 4, 3, 10], 31) # -> 8
    print(res)
    # the 8 subarrays that have a product less than 31 are:
    # [2] 
    # [4] 
    # [2, 4] 
    # [3]
    # [4, 3]
    # [2, 4, 3]
    # [3, 10]
    # [10]

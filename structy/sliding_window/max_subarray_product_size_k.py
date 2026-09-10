from math import inf, prod

def max_subarray_product_size_k(nums, k):
    max_product = -inf
    for i in range(0, len(nums) - k + 1):
        product = prod(nums[i:i + k])
        if product > max_product:
            max_product = product
    return max_product

def max_subarray_product_size_k_2(nums, k):
    max_product = -inf
    current_product = prod(nums[0:k])
    
    for i in range(0, len(nums) - k):
        current_product /= nums[i]
        current_product *= nums[i + k]
        if current_product > max_product:
            max_product = current_product

    return max_product

def driver():
    res = max_subarray_product_size_k_2([4, 2, 1, -9, 8, 2, 3], 3) # -> 48
    print(res)
    # [8,2,3] is the subarray of size 3 with the maximal product

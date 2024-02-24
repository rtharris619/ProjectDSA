from typing import List
from functools import reduce
from operator import mul


def product(nums: List[int]) -> List[int]:
    result = []

    total_product = reduce(mul, nums)
    result = [total_product // num for num in nums]

    return result


def product_2(nums: List[int]) -> List[int]:
    result = []

    current = 0
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if j != current:
                prod = prod * nums[j]
        result.append(prod)
        current += 1

    return result


def product_3(nums: List[int]) -> List[int]:
    pass


def solve():
    nums = [1, 2, 3, 4, 5]
    result = product_2(nums)
    print(result)

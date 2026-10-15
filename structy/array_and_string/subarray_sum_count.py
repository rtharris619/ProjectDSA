# Write a function, subarray_sum_count, that takes in an list of numbers and a targetSum. 
# The function should return the number of subarrays that sum to the given target.
# A subarray is a consecutive series of one or more elements of the list.

from collections import Counter

def subarray_sum_count(numbers, target_sum):
    prefix_sum = [0]
    total = 0
    for num in numbers:
        total += num
        prefix_sum.append(total)

    count = 0
    seen = Counter()
    for num in prefix_sum:        
        complement = num - target_sum
        count += seen[complement]
        seen[num] += 1

    return count

def driver():
    res = subarray_sum_count([1, 3, 1, 4, -2, 3], 5) # -> 3
    print(res)

    res = subarray_sum_count([1, 3, 1, 4, 3], 5) # -> 2
    print(res)
    
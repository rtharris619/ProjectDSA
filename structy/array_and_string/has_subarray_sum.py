def has_subarray_sum(numbers, target_sum):
    prefix_sum = [0]
    total = 0
    for num in numbers:
        total += num
        prefix_sum.append(total)
    seen = set()
    for num in prefix_sum:
        complement = num - target_sum
        if complement in seen:
            return True
        seen.add(num)
    return False

def driver():
    res = has_subarray_sum([1, 3, 1, 4, 3], 8) # -> True
    print(res)

    res = has_subarray_sum([1, 3, 1, 4, 3], 2) # -> False
    print(res)

    res = has_subarray_sum([5], 5) # -> True
    print(res)
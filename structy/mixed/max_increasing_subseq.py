# Write a function, max_increasing_subseq, that takes in a list of numbers as an argument.
# The function should return the length of the longest subsequence of strictly increasing numbers.

# A subsequence of a list can be created by deleting any items of the list,
# while maintaining the relative order of items.


from math import inf


def max_increasing_subseq(numbers):
    return _max_increasing_subseq(numbers, 0, -inf, {})


def _max_increasing_subseq(numbers, i, previous, memo):
    key = (i, previous)
    if key in memo:
        return memo[key]
    if i == len(numbers):
        return 0
    
    current = numbers[i]
    options = []
    dont_take_current = _max_increasing_subseq(numbers, i + 1, previous, memo)
    options.append(dont_take_current)
    if current > previous:
        take_current = 1 + _max_increasing_subseq(numbers, i + 1, current, memo)
        options.append(take_current)
    
    res = max(options)
    memo[key] = res
    return res


def driver():
    numbers = [4, 18, 20, 10, 12, 15, 19]
    res = max_increasing_subseq(numbers) # -> 5
    print(res)

    numbers = [
        1, 2, 300, 3, 4, 305, 5, 10, 7, 10, 6, 12, 6, 30, 7, 8, 9, 10, 10, 16, 14, 9, 10, 15, 11, 12, 13, 
        10, 18, 14, 15, 16, 17, 18, 19, 20, 21, 100,101 ,102, 103, 104, 105
    ]
    res = max_increasing_subseq(numbers) # -> 27
    print(res)
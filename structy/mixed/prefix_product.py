# Write a function, prefixProduct, that takes in a list of numbers.
# The function should return a new list of the same length where each element contains the running product up to that index
# of the original list.

# For example, the i-th result should be the product of all elements 0 to i:
# result[i] = numbers[0] * numbers[1] * numbers[2] * ... * numbers[i]

# You can assume that the input list is non-empty.


def prefix_product(numbers):
    res = []
    total = 1
    for num in numbers:
        total *= num
        res.append(total)
    return res

def driver():
    res = prefix_product([4, 2, 1, 6, 3, 6]) # -> [ 4, 8, 8, 48, 144, 864 ] 
    print(res)

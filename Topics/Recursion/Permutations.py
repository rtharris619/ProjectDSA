

def permutation_count(i, result):
    if i == 0:
        return result

    return permutation_count(i - 1, result * i)


def solve():
    nums = list(range(1, 6))
    # permutations(nums)
    result = permutation_count(len(nums), 1)
    print(nums, "->", result, "permutations.")

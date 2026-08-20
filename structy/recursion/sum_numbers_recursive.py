def sum_numbers_recursive(numbers: list[int]) -> int:
    def sum_nums(index: int, sum_so_far: int):
        if index == len(numbers):
            return sum_so_far
        sum_so_far += numbers[index]
        return sum_nums(index + 1, sum_so_far)

    return sum_nums(0, 0)

def sum_numbers_recursive_2(numbers: list[int]) -> int:
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_numbers_recursive_2(numbers[1:])

def driver():
    nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    res = sum_numbers_recursive_2(nums)
    print(res)
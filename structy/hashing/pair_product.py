def pair_product(numbers: list[int], target_product: int) -> tuple[int, int]:
    prev: dict[int, int] = {}
    for i, num in enumerate(numbers):
        complement = target_product / num
        if complement in prev:
            return (prev[complement], i)
        prev[num] = i

def driver():
    nums = [3, 2, 5, 4, 1]
    target = 8
    res = pair_product(nums, target)
    print(res)
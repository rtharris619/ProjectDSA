def pair_sum(numbers: list[int], target_sum: int) -> tuple[int, int]:
    prev: dict[int, int] = {}
    for i, num in enumerate(numbers):
        complement = target_sum - num
        if complement in prev:
            return (prev[complement], i)
        prev[num] = i

def driver():
    numbers = [3, 2, 5, 4, 1]
    target = 8
    res = pair_sum(numbers, target)
    print(res)
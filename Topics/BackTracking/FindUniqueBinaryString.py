from typing import List


def find_different_binary_string(nums: List[str]) -> str:
    str_set = {s for s in nums}

    def backtrack(i: int, cur: List[str]):
        if i == len(nums):
            result = "".join(cur)
            return None if result in str_set else result

        result = backtrack(i + 1, cur)
        if result:
            return result

        cur[i] = "1"
        result = backtrack(i + 1, cur)
        if result:
            return result

    return backtrack(0, ["0" for c in nums])


def solve():
    example1 = ["01", "10"]

    example2 = ["00", "01"]

    example3 = ["111", "011", "001"]

    result = find_different_binary_string(example2)
    print(result)

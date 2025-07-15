from typing import List


def permute(nums: List[int]) -> List[List[int]]:
  result = []

  if (len(nums) == 1):
    return [nums[:]]

  for _ in range(len(nums)):
    n = nums.pop(0)
    perms = permute(nums)

    for perm in perms:
      perm.append(n)
    result.extend(perms)
    nums.append(n)

  return result


def tests():
  nums = [1,2,3]
  print(permute(nums))


def driver():
  tests()

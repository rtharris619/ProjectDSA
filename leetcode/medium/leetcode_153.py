from typing import List


def find_min(nums: List[int]) -> int:

  minimum = float('infinity')

  L, R = 0, len(nums) - 1

  while L <= R:
    M = (L + R) // 2
    minimum = min(minimum, min(nums[M], nums[L]))

    if nums[M] >= nums[L]:
      L = M + 1
    else:
      R = M - 1

  return minimum


def tests():
  nums = [3,4,5,1,2]
  print(find_min(nums))

  nums = [4,5,6,7,0,1,2]
  print(find_min(nums))

  nums = [11,13,15,17]
  print(find_min(nums))

def driver():
  tests()

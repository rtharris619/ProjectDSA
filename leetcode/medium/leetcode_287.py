from typing import List

def find_duplicate(nums: List[int]) -> int:

  slow, fast = 0, 0
  while True:
    slow = nums[slow]
    fast = nums[nums[fast]]

    if slow == fast:
      break

  slow2 = 0
  while True:
    slow = nums[slow]
    slow2 = nums[slow2]
    if slow == slow2:
      return slow


def tests():
  nums = [1,3,4,2,2,5,6,7]
  res = find_duplicate(nums)
  print(res)


def driver():
  tests()

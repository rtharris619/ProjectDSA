from typing import List


def search(nums: List[int], target: int) -> int:

  def binary_search(left, right):
    if left > right:
      return -1
    
    mid = (left + right) // 2

    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      return binary_search(left, mid - 1)
    else:
      return binary_search(mid + 1, right)

  
  return binary_search(0, len(nums) - 1)


def search2(nums: List[int], target: int) -> int:
  L = 0
  R = len(nums) - 1

  while L <= R:
    mid = (R + L) // 2
    if nums[mid] < target:
      L = mid + 1
    elif nums[mid] > target:
      R = mid - 1
    else:
      return mid

  return -1


def tests():
  nums = [-1,0,3,5,9,12]
  target = 9
  res = search2(nums, target)
  print(res)

  nums = [-1,0,3,5,9,12]
  target = 2
  res = search2(nums, target)
  print(res)


def driver():
  tests()

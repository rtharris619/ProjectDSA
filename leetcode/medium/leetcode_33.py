from typing import List


def search(nums: List[int], target: int) -> int:
  
  L = 0
  R = len(nums) - 1

  while L <= R:
    mid = (L + R) // 2

    if target == nums[mid]:
      return mid
   
    # left sorted portion
    if nums[L] < nums[mid]:
      if target < nums[L] or target > nums[mid]:
        L = mid + 1
      else:
        R = mid - 1
    else: # right sorted portion
      if target > nums[R] or target < nums[mid]:
        R = mid - 1
      else:
        L = mid + 1
  
  return -1


def tests():
  nums, target = [4,5,6,7,0,1,2], 0
  print(search(nums, target))

  nums, target = [4,5,6,7,0,1,2], 3
  print(search(nums, target))


def driver():
  tests()

from typing import List

class Solution:
  def canPartition(self, nums: List[int]) -> bool:
    if sum(nums) % 2 > 0: # if NOT divisible by 2
      return False

    cache = set()
    cache.add(0)
    target = sum(nums) // 2

    for i in range(len(nums)):
      tmp = set()
      for item in cache:
        if nums[i] + item == target:
          return True
        tmp.add(item)
        tmp.add(nums[i] + item)
      cache = tmp
    return False
      

def tests():
  nums = [1,5,11,5]
  res = Solution().canPartition(nums)
  print(res)

  nums = [1,2,3,5]
  res = Solution().canPartition(nums)
  print(res)

def driver():
  tests()

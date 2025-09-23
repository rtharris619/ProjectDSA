from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    result = len(nums)
    for i in range(len(nums)):
      result = result ^ (i ^ nums[i])
    return result
  
  def missingNumber2(self, nums: List[int]) -> int:
    result = len(nums)
    for i in range(len(nums)):
      result += (i - nums[i])
    return result


def tests():
  nums = [3,0,1]
  print(Solution().missingNumber(nums))
  nums = [9,6,4,2,3,5,7,0,1]
  print(Solution().missingNumber2(nums))

def driver():
  tests()

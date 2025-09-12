from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    maxCurrent, currentSum = nums[0], 0
    for n in nums:
      if currentSum < 0:
        currentSum = 0
      currentSum += n
      maxCurrent = max(maxCurrent, currentSum)
    return maxCurrent

def tests():
  nums = [-2,1,-3,4,-1,2,1,-5,4]
  print(Solution().maxSubArray(nums))

def driver():
  tests()

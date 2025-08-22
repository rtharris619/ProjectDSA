from typing import List

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    
    result = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
      if n == 0:
        curMin, curMax = 1, 1
        continue
      temp = curMax * n
      curMax = max(n * curMax, n * curMin, n)
      curMin = min(temp, n * curMin, n)
      result = max(result, curMax)

    return result
  

def tests():
  nums = [2,3,-2,5,2]
  result = Solution().maxProduct(nums)
  print(result)


def driver():
  tests()

from typing import List

class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    cache = {} # (i, total) = # of ways

    def dfs(i: int, total: int):
      if i == len(nums):
        return 1 if total == target else 0
      if (i, total) in cache:
        return cache[(i, total)]
      
      cache[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
      return cache[(i, total)]
    
    return dfs(0, 0)
  

def tests():
  nums, target = [1,1,1,1,1], 3
  res = Solution().findTargetSumWays(nums, target)
  print(res)

def driver():
  tests()

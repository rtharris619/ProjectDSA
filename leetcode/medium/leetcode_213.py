from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    if len(nums) == 2:
      return max(nums[0], nums[1])

    def dfs(i: int, memo: dict, first: bool) -> int:
      if first and i >= len(nums) - 1: # don't include last house
        return 0
      if not first and i >= len(nums):
        return 0
      
      if i in memo:
        return memo[i]
      
      current = nums[i] + dfs(i + 2, memo, first)
      skip = dfs(i + 1, memo, first) # skip next house

      memo[i] = max(current, skip)
      return memo[i]
    
    memo1, memo2 = {}, {}
    return max(dfs(0, memo1, True), dfs(1, memo2, False))
  

  def rob2(self, nums: List[int]) -> int:

    def subRob(subNums: List[int]):
      a, b = 0, 0
      for num in subNums:
        a, b = b, max(num + a, b)
      return b

    return max(subRob(nums[1:]), subRob(nums[:-1]))


def tests():
  nums = [2,3,2]
  res = Solution().rob2(nums)
  print(res)
  nums = [1,2,3,1]
  res = Solution().rob2(nums)
  print(res)
  nums = [1,2,3]
  res = Solution().rob2(nums)
  print(res)
  # nums = [1]
  # res = Solution().rob(nums)
  # print(res)
  nums = [6,6,4,8,4,3,3,10]
  res = Solution().rob2(nums)
  print(res)


def driver():
  tests()

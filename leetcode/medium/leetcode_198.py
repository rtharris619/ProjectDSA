from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    memo = {}

    def dfs(step: int) -> int:
      if step >= len(nums):
        return 0
      
      if step in memo:
        return memo[step]
      
      amt = nums[step] + max(dfs(step + 2), dfs(step + 3))
      memo[step] = amt

      return amt

    return max(dfs(0), dfs(1))
  

  def rob2(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    if len(nums) == 2:
      return max(nums[0], nums[1])
    
    nums.append(0) # [2,1,1,0]

    for i in range(len(nums) - 4, -1, -1):
      nums[i] += max(nums[i + 2], nums[i + 3])

    return max(nums[0], nums[1])
  
  
  def rob3(self, nums: List[int]) -> int:
    a, b = 0, 0
    for n in nums:
      a, b = b, max(n + a, b)
    return b


def tests():
  nums = [1,2,3,1]
  res = Solution().rob3(nums)
  print(res)

  nums = [2,7,9,3,1]
  res = Solution().rob3(nums)
  print(res)

  nums = [2,1,1,2]
  res = Solution().rob3(nums)
  print(res)

  nums = [2,1,1]
  res = Solution().rob3(nums)
  print(res)


def driver():
  tests()

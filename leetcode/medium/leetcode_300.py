from typing import List

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
      for j in range(i + 1, len(nums)):
        if nums[i] < nums[j]:
          LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)
  

def tests():
  nums = [1,2,4,3]
  res = Solution().lengthOfLIS(nums)
  print(res)


def driver():
  tests()

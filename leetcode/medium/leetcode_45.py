from typing import List

class Solution:
  def jump(self, nums: List[int]) -> int:
    L = R = 0
    jumps = 0

    while R < len(nums) - 1:
      F = 0
      for i in range(L, R + 1):
        F = max(F, nums[i] + i)
      L = R + 1
      R = F
      jumps += 1

    return jumps
  

def tests():
  nums = [2,3,1,1,4]
  print(Solution().jump(nums))


def driver():
  tests()

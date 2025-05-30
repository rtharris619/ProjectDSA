from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
  result = []
  nums.sort()

  for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    left, right = i + 1, len(nums) - 1
    while left < right:
      threeSum = nums[i] + nums[left] + nums[right]
      if threeSum > 0:
        right -= 1
      elif threeSum < 0:
        left += 1
      else:
        result.append([nums[i], nums[left], nums[right]])
        left += 1
        while nums[left] == nums[left - 1] and left < right:
          left += 1

  return result


def tests():
  nums = [-3,3,4,-3,1,2] # [-3,-3,1,2,3,4]
  result = three_sum(nums)
  print(result)

def driver():
  tests()

from typing import List


def subsets_two(nums: List[int]) -> List[List[int]]:
  result = []
  nums.sort()

  subset = []
  def backtrack(i: int):
    if i >= len(nums):
      temp = subset[:]
      if temp not in result:
        result.append(temp)
      return
        
    subset.append(nums[i])
    backtrack(i + 1)

    subset.pop()
    backtrack(i + 1)

  backtrack(0)

  return result


def subsets_two_2(nums: List[int]) -> List[List[int]]:
  result = []
  nums.sort()

  def backtrack(i: int, subset: List[int]):
    if i >= len(nums):
      result.append(subset[:])
      return
    
    subset.append(nums[i])
    backtrack(i + 1, subset)
    subset.pop()

    while i + 1 < len(nums) and nums[i] == nums[i+1]:
      i += 1
    backtrack(i + 1, subset)

  backtrack(0, [])

  return result


def tests():
  nums = [1,2,2]
  print(subsets_two_2(nums))
  nums = [0]
  print(subsets_two(nums))
  nums = [4,4,4,1,4]
  print(subsets_two(nums))


def driver():
  tests()

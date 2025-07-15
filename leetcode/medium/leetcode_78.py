from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
  result = []

  subset = []
  def backtrack(i: int):
    if i >= len(nums):
      result.append(subset[:])
      return
    
    # decision to include nums[i]
    subset.append(nums[i])
    backtrack(i + 1)

    # decision NOT to include nums[i]
    subset.pop()
    backtrack(i + 1)

  backtrack(0)

  return result


def tests():
  nums = [1,2,3]
  print(subsets(nums))
  nums = [1,2,2]
  print(subsets(nums))


def driver():
  tests()

from typing import List

def two_sum(numbers: List[int], target: int):
  left = 0
  right = len(numbers) - 1

  while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum > target:
      right -= 1
    elif current_sum < target:
      left += 1
    else:
      return [left+1,right+1]
    
  return []


def tests():
  result = two_sum([1,3,4,5,7,10,11], 9)
  print(result)


def driver():
  tests()

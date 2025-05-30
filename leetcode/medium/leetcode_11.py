from typing import List

def max_area(height: List[int]):
  max_area = 0
  for i in range(len(height)):
    for j in range(i + 1, len(height)):
      area = min(height[i], height[j]) * (j - i)
      max_area = max(area, max_area)

  return max_area

def max_area2(height: List[int]):
  max_area = 0
  left = 0
  right = len(height) - 1

  while left < right:
    area = min(height[left], height[right]) * (right - left)
    max_area = max(area, max_area)

    if height[left] > height[right]:
      right -= 1
    elif height[left] <= height[right]:
      left += 1

  return max_area


def tests():
  height = [1,8,6,2,5,4,8,3,7]
  result = max_area2(height)
  print(result)
  height = [1,1]
  result = max_area2(height)
  print(result)


def driver():
  tests()

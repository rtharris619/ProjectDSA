from typing import List

def largest_rectangle_area(heights: List[int]) -> int:
  max_area = 0
  stack = []

  for i, height in enumerate(heights):
    start = i
    while stack and stack[-1][1] > height:
      stack_i, stack_height = stack.pop()
      max_area = max(max_area, stack_height * (i - stack_i))
      start = stack_i
    stack.append([start, height])

  for i, height in stack:
    max_area = max(max_area, height * (len(heights) - i))

  return max_area


def tests():
  heights = [2,1,5,6,2,3]
  res = largest_rectangle_area(heights)
  print(res)

  heights = [2,4]
  res = largest_rectangle_area(heights)
  print(res)


def driver():
  tests()

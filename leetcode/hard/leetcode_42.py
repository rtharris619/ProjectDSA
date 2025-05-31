from typing import List


def trap(height: List[int]) -> int:

  # Has water function:
  # min(max(maxL, maxR)) - h[i] > 0
  # take minimum of max height between L and R
  # shift the smaller of the two pointers

  L = 0
  R = len(height) - 1
  maxL = height[L]
  maxR = height[R]

  water = 0
  current = 0

  while L < R:

    if maxL <= maxR:
      L += 1
      maxL = max(height[L], maxL)
      current = L
    else:
      R -= 1
      maxR = max(height[R], maxR)
      current = R

    if min(maxL, maxR) - height[current] > 0:
      water += min(maxL, maxR) - height[current]

  return water


def tests():
  height = [0,1,0,2,1,0,1,3,2,1,2,1]
  result = trap(height)
  print(result)

  height = [4,2,0,3,2,5]
  result = trap(height)
  print(result)


def driver():
  tests()

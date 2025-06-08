from typing import List
from collections import deque


def max_sliding_window(nums: List[int], k: int) -> List[int]:
  output = []

  my_deque = deque()

  L = R = 0

  while R < len(nums):
    # pop smaller values from deque
    while my_deque and nums[my_deque[-1]] < nums[R]:
      my_deque.pop()

    my_deque.append(R)

    # remove left value from window
    if L > my_deque[0]:
      my_deque.popleft()

    if (R + 1) >= k:
      output.append(nums[my_deque[0]])
      L += 1

    R += 1

  return output


def tests():
  nums = [8,7,6,9]
  k = 2
  res = max_sliding_window(nums, k)
  print(res)
  nums = [1,3,-1,-3,5,3,6,7]
  k = 3
  res = max_sliding_window(nums, k)
  print(res)

def driver():
  tests()

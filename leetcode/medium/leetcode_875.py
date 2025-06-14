from typing import List
import math


def min_eating_speed(piles: List[int], h: int) -> int:

  KMin = 1
  KMax = max(piles)

  result = KMax

  while KMin <= KMax:
    k = (KMin + KMax) // 2

    time = 0
    for p in piles:
      time += math.ceil(p / k)
    
    if time > h:
      KMin = k + 1
    elif time <= h:
      result = min(result, k)
      KMax = k - 1

  return result


def tests():
  piles = [3,6,7,11]
  h = 8
  print(min_eating_speed(piles, h))

  piles = [30,11,23,4,20]
  h = 5
  print(min_eating_speed(piles, h))

  piles = [30,11,23,4,20]
  h = 6
  print(min_eating_speed(piles, h))

  piles = [1,1,1,999999999]
  h = 10
  print(min_eating_speed(piles, h))

def driver():
  tests()

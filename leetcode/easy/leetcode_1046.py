from typing import List
import heapq


def last_stone_weight(stones: List[int]) -> int:

  maxheap = [-stone for stone in stones]
  heapq.heapify(maxheap)

  while len(maxheap) > 1:
    x = abs(heapq.heappop(maxheap))
    y = abs(heapq.heappop(maxheap))
    if x != y:
      heapq.heappush(maxheap, -(x - y))

  return 0 if len(maxheap) == 0 else abs(maxheap[0])


def tests():
  stones = [2,7,4,1,8,1]
  print(last_stone_weight(stones))

  stones = [7,5,8]
  print(last_stone_weight(stones))


def driver():
  tests()

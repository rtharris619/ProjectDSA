from typing import List
import heapq
import math


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
  heap = []
  for i, point in enumerate(points):
    distance = math.sqrt(point[0]**2 + point[1]**2)
    heap.append((distance, i))

  heapq.heapify(heap)

  result = []
  while k > 0:
    item = heapq.heappop(heap)
    result.append(points[item[1]])
    k -= 1

  return result


def tests():
  points, k = [[1,3], [-2,2]], 1
  print(k_closest(points, k))

  points, k = [[3,3], [5,-1], [-2,4]], 2
  print(k_closest(points, k))


def driver():
  tests()

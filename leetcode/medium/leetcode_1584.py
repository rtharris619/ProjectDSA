from typing import List
import heapq

class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    n = len(points)
    adjacencies = {i: [] for i in range(n)} # list of [cost, node]

    for i in range(n):
      x1, y1 = points[i]
      for j in range(i + 1, n):
        x2, y2 = points[j]
        cost = abs(x1 - x2) + abs(y1 - y2)
        adjacencies[i].append([cost, j])
        adjacencies[j].append([cost, i])

    print(adjacencies)

    visited = set()
    minHeap = [[0, 0]]
    result = 0

    while n > len(visited):
      cost, i = heapq.heappop(minHeap)
      if i in visited:
        continue
      visited.add(i)
      result += cost
      for neighborCost, neighbor in adjacencies[i]:
        if neighbor not in visited:
          heapq.heappush(minHeap, [neighborCost, neighbor])

    return result


def tests():
  points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
  res = Solution().minCostConnectPoints(points)
  print(res)


def driver():
  tests()

from typing import List
from collections import defaultdict
import heapq

class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    overallTime = 0

    adjacencies = defaultdict(list)
    for node, neighbor, time in times:
      adjacencies[node].append([neighbor, time])
    print(adjacencies)

    minHeap = [[0, k]]
    visited = set()

    while minHeap:
      time, node = heapq.heappop(minHeap)
      if node in visited:
        continue
      visited.add(node)
      overallTime = max(overallTime, time)

      for neighbor, neighborTime in adjacencies[node]:
        if neighbor not in visited:
          heapq.heappush(minHeap, [time + neighborTime, neighbor])

    return overallTime if len(visited) == n else -1


def tests():
  times, n, k = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
  result = Solution().networkDelayTime(times, n, k)
  print(result)

def driver():
  tests()

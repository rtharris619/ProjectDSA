from typing import Counter, List
import heapq
from collections import deque


def least_interval(tasks: List[str], n: int) -> int:
  time = 0
  queue = deque()

  counts = Counter(tasks)
  heap = [-count for count in counts.values()]
  heapq.heapify(heap)

  while heap or queue:
    time += 1
    if heap:
      count = 1 + heapq.heappop(heap)
      if count:
        queue.append([count, time + n])
    if queue and queue[0][1] == time:
      heapq.heappush(heap, queue.popleft()[0])

  return time


def test1():
  tasks, n = ["A", "A", "A", "B", "B", "C", "C"], 1
  print(least_interval(tasks, n))


def test2():
  tasks, n = ["A", "A", "A", "B", "B", "B"], 2
  print(least_interval(tasks, n))


def tests():
  test1()
  test2()


def driver():
  tests()

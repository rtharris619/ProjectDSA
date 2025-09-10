from typing import List

class Interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end

class Solution:
  def min_meeting_rooms(self, intervals: List[Interval]) -> int:
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    result, count = 0, 0
    S, E = 0, 0

    while S < len(intervals):
      if start[S] < end[E]:
        count += 1
        S += 1
      else:
        count -= 1
        E += 1
      result = max(result, count)
    
    return count


def tests():
  intervals = [Interval(0,30), Interval(5,10), Interval(15,20)]
  print(Solution().min_meeting_rooms(intervals))

def driver():
  tests()

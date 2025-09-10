from typing import List

class Interval(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end

class Solution:
  def can_attend_meetings(self, intervals: List[Interval]) -> bool:
    intervals.sort(key = lambda i : i.start)

    for i in range(1, len(intervals)):
      intervalOne = intervals[i - 1]
      intervalTwo = intervals[i]
      if intervalOne.end > intervalTwo.start:
        return False

    return True
  

def tests():
  intervals = list([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) 
  print(Solution().can_attend_meetings(intervals))

  intervals = list([Interval(5,8), Interval(9,15)])
  print(Solution().can_attend_meetings(intervals))

def driver():
  tests()

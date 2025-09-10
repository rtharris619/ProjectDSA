from typing import List

class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    result = 0

    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
      if start >= prevEnd:
        prevEnd = end
      else:
        result += 1
        prevEnd = min(prevEnd, end)

    return result
  

def tests():
  intervals = [[1,2],[2,3],[3,4],[1,3]]
  print(Solution().eraseOverlapIntervals(intervals))

def driver():
  tests()

from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda i : i[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
      lastEnd = result[-1][1]
      if start <= lastEnd:
        result[-1][1] = max(lastEnd, end)
      else:
        result.append([start, end])

    return result
  
def tests():
  intervals = [[1,3],[2,6],[8,10],[15,18]]
  print(Solution().merge(intervals))

def driver():
  tests()

from typing import List
from collections import deque


class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    result = []
    ROWS, COLS = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(row: int, col: int, visited: set, prevHeight: int):
      if (row, col) in visited or row < 0 or col < 0 or row == ROWS or col == COLS or heights[row][col] < prevHeight:
        return
      visited.add((row, col))
      directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
      for dr, dc in directions:
        rown, coln = row + dr, col + dc
        dfs(rown, coln, visited, heights[row][col])

    for col in range(COLS):
      dfs(0, col, pacific, heights[0][col])
      dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col])

    for row in range(ROWS):
      dfs(row, 0, pacific, heights[row][0])
      dfs(row, COLS - 1, atlantic, heights[row][COLS - 1])

    for row in range(ROWS):
      for col in range(COLS):
        if (row, col) in pacific and (row, col) in atlantic:
          result.append([row, col])

    return result
  

def tests():
  heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]]
  result = Solution().pacificAtlantic(heights)
  print(result)

  # heights = [[1]]
  # print(Solution().pacificAtlantic(heights))


def driver():
  tests()

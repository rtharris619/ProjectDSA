from typing import List
import collections


class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    maxArea = 0
    visited = set()

    def bfs(row: int, col: int):
      area = 1
      queue = collections.deque()
      queue.append((row, col))
      visited.add((row, col))

      while queue:
        r, c = queue.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
          rn, cn = dr + r, dc + c
          if rn in range(ROWS) and cn in range(COLS) and grid[rn][cn] == 1 and (rn, cn) not in visited:
            queue.append((rn, cn))
            visited.add((rn, cn))
            area += 1

      return area

    for row in range(ROWS):
      for col in range(COLS):
        if grid[row][col] == 1 and (row, col) not in visited:
          area = bfs(row, col)
          maxArea = max(maxArea, area)

    return maxArea


  def maxAreaOfIsland_2(self, grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    maxArea = 0
    visited = set()

    def dfs(row: int, col: int) -> int:
      if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0 or (row, col) in visited:
        return 0
      visited.add((row, col))
      return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
    
    for row in range(ROWS):
      for col in range(COLS):
        if (row, col) not in visited and grid[row][col] == 1:
          area = dfs(row, col)
          maxArea = max(maxArea, area)
    
    return maxArea


def tests():
  grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
  result = Solution().maxAreaOfIsland_2(grid)
  print('Max area is', result)

  grid = [[0,0,0,0,0,0,0,0]]
  print(Solution().maxAreaOfIsland_2(grid))


def driver():
  tests()

from typing import List
import collections

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
      return 0
    
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(row: int, col: int):
      q = collections.deque()
      q.append((row, col))
      visited.add((row, col))

      while q:
        r, c = q.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
          rn, cn = dr + r, dc + c
          if (rn in range(ROWS) and cn in range(COLS) and (rn, cn) not in visited and grid[rn][cn] == "1"):
            visited.add((rn, cn))
            q.append((rn, cn))

    for row in range(ROWS):
      for col in range(COLS):
        if grid[row][col] == "1" and (row, col) not in visited:
          bfs(row, col)
          islands += 1

    return islands


def tests():
  grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  print(Solution().numIslands(grid))

  grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  print(Solution().numIslands(grid))

  grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]]
  print(Solution().numIslands(grid))


def driver():
  tests()

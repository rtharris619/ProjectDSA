from typing import List
from collections import deque

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()
    fresh, time = 0, 0

    for row in range(ROWS):
      for col in range(COLS):
        if grid[row][col] == 1:
          fresh += 1
        if grid[row][col] == 2:
          q.append([row, col])

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q and fresh > 0:
      for _ in range(len(q)):
        row, col = q.popleft()
        for dr, dc in directions:
          newRow, newCol = row + dr, col + dc
          if newRow < 0 or newCol < 0 or newRow == ROWS or newCol == COLS or grid[newRow][newCol] != 1:
            continue
          grid[newRow][newCol] = 2
          q.append([newRow, newCol])
          fresh -= 1
      time += 1

    return time if fresh == 0 else -1
  

def tests():
  grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]]
  result = Solution().orangesRotting(grid)
  print(result)

  grid = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
  ]
  result = Solution().orangesRotting(grid)
  print(result)

def driver():
  tests()

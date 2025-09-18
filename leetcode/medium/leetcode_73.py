from typing import List

class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    for r in range(ROWS):
      for c in range(COLS):
        if matrix[r][c] == 0:
          matrix[0][c] = 0 # mark all cols of row0 to zero.
          if r > 0:
            matrix[r][0] = 0 # mark all rows of col0 to zero.
          else:
            rowZero = True

    for r in range(1, ROWS):
      for c in range(1, COLS):
        if matrix[0][c] == 0 or matrix[r][0] == 0:
          matrix[r][c] = 0

    if matrix[0][0] == 0:
      for r in range(ROWS):
        matrix[r][0] = 0 # mark all rows of col0 to zero.

    if rowZero:
      for c in range(COLS):
        matrix[0][c] = 0 # mark all cols of row0 to zero.

    print(matrix)


def tests():
  matrix = [[1,1,1],[1,0,1],[1,1,1]]
  Solution().setZeroes(matrix)
  matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
  Solution().setZeroes(matrix)

def driver():
  tests()

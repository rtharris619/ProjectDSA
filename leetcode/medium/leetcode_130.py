from typing import List

class Solution:
  def solve(self, board: List[List[str]]) -> None:
    ROWS, COLS = len(board), len(board[0])

    # 1. Capture unsurrounded regions (O -> T)
    def dfs(row: int, col: int):
      if row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] != "O":
        return
      board[row][col] = "T"
      dfs(row + 1, col)
      dfs(row - 1, col)
      dfs(row, col + 1)
      dfs(row, col - 1)
      
    for row in range(ROWS):
      for col in range(COLS):
        if board[row][col] == "O" and (row in [0, ROWS - 1] or col in [0, COLS - 1]):
          dfs(row, col)

    # 2. Capture surrounded regions (O -> X)
    for row in range(ROWS):
      for col in range(COLS):
        if board[row][col] == "O":
          board[row][col] = "X"

    # 3. Uncapture unsurrounded regions (T -> O)
    for row in range(ROWS):
      for col in range(COLS):
        if board[row][col] == "T":
          board[row][col] = "O"


  def printBoard(self, board: List[List[str]]):
    print('\nBoard:')
    for row in range(len(board)):
      for col in range(len(board[0])):
        print(board[row][col], end=" ")
      print()


def tests():
  board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]
  sol = Solution()
  sol.solve(board)
  sol.printBoard(board)

  board = [["X"]]
  sol.solve(board)
  sol.printBoard(board)

  board = [
    ["O","O"],
    ["O","O"]]
  sol.solve(board)
  sol.printBoard(board)

  board = [
    ["O","X","O"],
    ["X","X","O"],
    ["O","O","O"]]
  sol.solve(board)
  sol.printBoard(board)


def driver():
  tests()

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
  path = set()
  
  ROWS, COLS = len(board), len(board[0])

  def backtrack(row: int, col: int, index: int):
    if index == len(word):
      return True
    if ((row < 0 or col < 0)
      or (row >= ROWS or col >= COLS)
      or (board[row][col] != word[index])
      or (row, col) in path):
      return False
    
    path.add((row, col))
    index += 1
    result = (backtrack(row + 1, col, index)
             or backtrack(row - 1, col, index)
             or backtrack(row, col + 1, index)
             or backtrack(row, col - 1, index))
    path.remove((row, col))

    return result
  
  for row in range(ROWS):
    for col in range(COLS):
      if board[row][col] == word[0] and backtrack(row, col, 0):
        return True
      
  return False


def tests():
  board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
  print(exist(board, word))
  board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"
  print(exist(board, word))
  board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"
  print(exist(board, word))


def driver():
  tests()

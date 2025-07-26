from typing import List
from collections import deque

INF = 2**31 - 1

class Solution:
  def wallsAndGates(self, rooms: List[List[int]]) -> None:
    ROWS, COLS = len(rooms), len(rooms[0])
    visited = set()
    q = deque()

    for row in range(ROWS):
      for col in range(COLS):
        if rooms[row][col] == 0:
          q.append([row, col])
          visited.add((row, col))
          
    distance = 1
    while q:
      for _ in range(len(q)):
        row, col = q.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
          newRow, newCol = dr + row, dc + col
          if (newRow < 0 
              or newCol < 0 
              or newRow == ROWS 
              or newCol == COLS 
              or rooms[newRow][newCol] != INF
              or (newRow, newCol) in visited):
            continue
          rooms[newRow][newCol] = distance
          q.append([newRow, newCol])
          visited.add((newRow, newCol))
      distance += 1

    print(rooms)

  def wallsAndGates2(self, rooms: List[List[int]]) -> None:
    ROWS, COLS = len(rooms), len(rooms[0])
    visited = set()
    q = deque()

    def addRoom(row: int, col: int):
      if (row < 0 
        or col < 0 
        or row == ROWS 
        or col == COLS 
        or rooms[row][col] != INF
        or (row, col) in visited):
        return
      q.append([row, col])
      visited.add((row, col))

    for row in range(ROWS):
      for col in range(COLS):
        if rooms[row][col] == 0:
          q.append([row, col])
          visited.add((row, col))

    distance = 0
    while q:
      for _ in range(len(q)):
        row, col = q.popleft()
        rooms[row][col] = distance

        addRoom(row + 1, col)
        addRoom(row - 1, col)
        addRoom(row, col + 1)
        addRoom(row, col - 1)
      distance += 1

    print(rooms)


def tests():  
  rooms = [
      [INF, -1, 0, INF],
      [INF, INF, INF, -1],
      [INF, -1, INF, -1],
      [0, -1, INF, INF]
    ]
  Solution().wallsAndGates(rooms)

  rooms = [
    [INF, INF, INF, 0],
    [INF, -1,  INF, INF],
    [0, INF, INF, INF]]
  Solution().wallsAndGates(rooms)


def driver():
  tests()

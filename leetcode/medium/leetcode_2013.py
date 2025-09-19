from collections import defaultdict
from typing import List

class DetectSquares:

  def __init__(self):
    self.pointsCount = defaultdict(int)
    self.points = []

  def add(self, point: List[int]) -> None:
    self.pointsCount[tuple(point)] += 1
    self.points.append(point)

  def count(self, point: List[int]) -> int:
    result = 0

    px, py = point
    for x, y in self.points:
      if (abs(px - x) != abs(py - y)) or x == px or y == py:
        continue
      result += self.pointsCount[(x, py)] * self.pointsCount[(px, y)]

    return result


def tests():
  squares = DetectSquares()
  squares.add([3, 10])
  squares.add([11, 2])
  squares.add([3, 2])
  print(squares.count([11, 10]))
  print(squares.count([14, 10]))
  squares.add([11, 2])
  print(squares.count([11, 10]))

def driver():
  tests()

from typing import List

class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    result = []
    L, R = 0, len(matrix[0])
    T, B = 0, len(matrix)

    while L < R and T < B:
      for i in range(L, R):
        result.append(matrix[T][i])
      T += 1

      for i in range(T, B):
        result.append(matrix[i][R - 1])
      R -= 1

      if not (L < R and T < B):
        break

      for i in range(R - 1, L - 1, -1):
        result.append(matrix[B - 1][i])
      B -= 1

      for i in range(B - 1, T - 1, -1):
        result.append(matrix[i][L])
      L += 1

    return result
  

def tests():
  matrix = [[1,2,3],[4,5,6],[7,8,9]]
  print(Solution().spiralOrder(matrix))

  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  print(Solution().spiralOrder(matrix))


def driver():
  tests()

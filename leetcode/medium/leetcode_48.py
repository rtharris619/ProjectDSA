from typing import List

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    L, R = 0, len(matrix) - 1
    while L < R:
      for i in range(R - L):
        T, B = L, R
        # 1. save top left
        topLeft = matrix[T][L + i]

        # 2. move bottom left into top left
        matrix[T][L + i] = matrix[B - i][L]

        # 3. move bottom right into bottom left
        matrix[B - i][L] = matrix[B][R - i]

        # 4. move top right into bottom right
        matrix[B][R - i] = matrix[T + i][R]

        # 5. move top left into top right
        matrix[T + i][R] = topLeft

      L += 1
      R -= 1
    print(matrix)


def tests(): 
  matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
  Solution().rotate(matrix)

def driver():
  tests()

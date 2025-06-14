from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:

  R = matrix[-1]
  RL = 0
  RR = len(matrix) - 1

  while RL <= RR:
    R = (RL + RR) // 2

    if matrix[R][0] <= target <= matrix[R][-1]:
      left = 0
      right = len(matrix[0])

      while left <= right:
        mid = (right + left) // 2
        if target == matrix[R][mid]:
          return True
        elif target > matrix[R][mid]:
          left = mid + 1
        elif target < matrix[R][mid]:
          right = mid - 1
      
      return False

    elif target < matrix[R][0]:
      RR = R - 1
    elif target > matrix[R][-1]:
      RL = R + 1

  return False


def tests():
  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
  target = 3
  res = search_matrix(matrix, target)
  print(res)

  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
  target = 13
  res = search_matrix(matrix, target)
  print(res)



def driver():
  tests()

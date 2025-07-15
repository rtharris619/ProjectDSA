from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
  result = []

  def backtrack(i: int, current: List[int], total: int):
    if total == target:
      result.append(current[:])
      return
    if i >= len(candidates) or total > target:
      return
    
    current.append(candidates[i])
    backtrack(i, current, total + candidates[i])

    current.pop()
    backtrack(i + 1, current, total)

  backtrack(0, [], 0)

  return result


def tests():
  candidates, target = [2,3,6,7], 7
  print(combination_sum(candidates, target))


def driver():
  tests()

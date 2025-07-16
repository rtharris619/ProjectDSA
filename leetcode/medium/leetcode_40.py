from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
  result = []
  candidates.sort()

  def backtrack(i: int, current: List[int], total: int):
    if total == target:
      result.append(current[:])
      return
    if i >= len(candidates) or total > target:
      return
    
    current.append(candidates[i])
    backtrack(i + 1, current, total + candidates[i])
    current.pop()

    while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
      i += 1
    backtrack(i + 1, current, total)

  backtrack(0, [], 0)
  return result


def tests():
  candidates, target = [10,1,2,7,6,1,5], 8
  print(combination_sum(candidates, target))


def driver():
  tests()

from typing import List

class Solution:
  def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
    result = set()

    for triplet in triplets:
      if triplet[0] > target[0] or triplet [1] > target[1] or triplet[2] > target[2]:
        continue
      for i, v in enumerate(triplet):
        if v == target[i]:
          result.add(i)

    return len(result) == 3


def tests():
  triplets, target = [[2,5,3],[1,8,4],[1,7,5]], [2,7,5]
  print(Solution().mergeTriplets(triplets, target))


def driver():
  tests()

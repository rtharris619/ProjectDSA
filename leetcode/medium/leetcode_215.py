from typing import List
import heapq


# Sorting solution is n*log(n)
def find_k_largest_1(nums: List[int], k: int) -> int:
  nums.sort()
  return nums[len(nums) - k]


# Heap solution is better than sorting solution [n + (k*log(n))]
def find_k_largest_2(nums: List[int], k: int) -> int:

  heapPositives = [-num for num in nums if num >= 0]
  heapq.heapify(heapPositives)

  while k > 0 and len(heapPositives) > 0:
    current = abs(heapq.heappop(heapPositives))
    k -= 1

  if k == 0:
    return current

  heapNegatives = [abs(num) for num in nums if num < 0]
  heapq.heapify(heapNegatives)

  while k > 0 and len(heapNegatives) > 0:
    current = -heapq.heappop(heapNegatives)
    k -= 1

  return current


# Quick Select algorithm has the best avg time complexity. Best case: [O(n)]
def find_k_largest_3(nums: List[int], k: int) -> int:
  K = len(nums) - k

  def quick_select(L, R):
    pivot, P = nums[R], L
    for i in range(L, R):
      if nums[i] <= pivot:
        nums[P], nums[i] = nums[i], nums[P]
        P += 1
    nums[P], nums[R] = nums[R], nums[P]

    if K < P:
      return quick_select(L, P - 1)
    elif K > P:
      return quick_select(P + 1, R)
    else:
      return nums[P]
    
  return quick_select(0, len(nums) - 1)


def tests():
  nums, k = [3,2,1,5,6,4], 2
  print(find_k_largest_3(nums, k))
  nums, k = [3,2,3,1,2,4,5,5,6], 4
  print(find_k_largest_3(nums, k))
  nums, k = [-1,-1], 2
  print(find_k_largest_3(nums, k))
  nums, k = [-1,2,6,-2], 3
  print(find_k_largest_3(nums, k))

def driver():
  tests()

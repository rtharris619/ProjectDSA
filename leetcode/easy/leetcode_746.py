from typing import List

class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    topFloor = len(cost)
    memo = {}
    
    def dfs(step: int):
      if step >= topFloor:
        return 0
      
      if step in memo:
        return memo[step]
      
      min_cost = cost[step] + min(dfs(step + 1), dfs(step + 2))
      memo[step] = min_cost

      return min_cost
      
    return min(dfs(0), dfs(1))
  
  
  def minCostClimbingStairs2(self, cost: List[int]) -> int:
    cost.append(0) # [10,15,20,0] -> [25,15,20,0]
    for i in range(len(cost) - 3, -1, -1):
      cost[i] += min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])


def tests():
  cost = [10,15,20]
  res = Solution().minCostClimbingStairs2(cost)
  print(res)
  cost = [1,100,1,1,1,100,1,1,100,1]
  res = Solution().minCostClimbingStairs2(cost)
  print(res)


def driver():
  tests()

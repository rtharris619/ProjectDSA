from typing import List

class Solution:
  def change(self, amount: int, coins: List[int]) -> int:
    
    cache = {}
    def dfs(i: int, a: int) -> int:
      if a == amount:
        return 1
      if i >= len(coins):
        return 0
      if a > amount:
        return 0
      if (i, a) in cache:
        return cache[(i, a)]
      
      cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
      return cache[(i, a)]
    
    return dfs(0, 0)
  
  def change2(self, amount: int, coins: List[int]) -> int:
    dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)

    for a in range(1, amount + 1):
      for i in range(len(coins) - 1, -1, -1):
        dp[a][i] = dp[a][i + 1]
        if a - coins[i] >= 0:
          dp[a][i] += dp[a - coins[i]][i]
    
    return dp[amount][0]


def tests():
  amount, coins = 5, [1,2,5]
  res = Solution().change2(amount, coins)
  print(res)

def driver():
  tests()

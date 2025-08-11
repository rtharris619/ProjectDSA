from typing import List
from collections import deque

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    if len(coins) == 1:
      if amount == 0:
        return 0
      return amount // coins[0] if amount % coins[0] == 0 else -1
    
    q = deque([(0,0)])
    visited = set([0])
      
    while q:
      current, total = q.popleft()
      
      for coin in coins:
        new = current + coin

        if new == amount:
          return total + 1
        
        if new < amount and new not in visited:
          visited.add(new)
          q.append((new, total + 1))

    return -1

  def coinChange2(self, coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for amt in range(1, amount + 1):
      for coin in coins:
        if amt - coin >= 0:
          dp[amt] = min(dp[amt], 1 + dp[amt - coin])

    return dp[amount] if dp[amount] != amount + 1 else -1
  

def tests():
  coins, amount = [1,2,5], 11
  res = Solution().coinChange2(coins, amount)
  print(res)

  # coins, amount = [2, 4, 6], 3
  # res = Solution().coinChange(coins, amount)
  # print(res)

  coins, amount = [1,2,5], 102 # 102, 51, 5
  res = Solution().coinChange2(coins, amount)
  print(res)
  

def driver():
  tests()

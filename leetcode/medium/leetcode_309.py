from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    dp = {}

    def dfs(i: int, buying: bool):
      if i >= len(prices):
        return 0
      if (i, buying) in dp:
        return dp[(i, buying)]
      
      cooldown = dfs(i + 1, buying)
      if buying:
        buy = dfs(i + 1, not buying) - prices[i]
        dp[(i, buying)] = max(cooldown, buy)
      else:
        sell = dfs(i + 2, not buying) + prices[i]
        dp[(i, buying)] = max(cooldown, sell)

      return dp[(i, buying)]
    
    return dfs(0, True)


def tests():
  prices = [1,2,3,0,2]
  res = Solution().maxProfit(prices)
  print(res)


def driver():
  tests()

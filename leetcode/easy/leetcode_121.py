from typing import List

def max_profit(prices: List[int]) -> int:
  max_profit = 0

  L, R = 0, 1

  while R < len(prices):
    if prices[R] > prices[L]:
      profit = prices[R] - prices[L]
      max_profit = max(profit, max_profit)
    else:
      L = R
    R += 1

  return max_profit


def tests():
  prices = [7,1,5,3,6,4]
  result = max_profit(prices)
  print(result)
  prices = [7,6,4,3,1]
  result = max_profit(prices)
  print(result)
  prices = [1,2,4,2,5,7,2,4,9,0,9]
  result = max_profit(prices)
  print(result)


def driver():
  tests()

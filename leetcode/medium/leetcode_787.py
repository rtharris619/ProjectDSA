from typing import List

class Solution:
  inf = float("inf")
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    prices = [self.inf] * n
    prices[src] = 0

    for _ in range(k + 1):
      tempPrices = prices[:]
      for s, d, p in flights:
        if prices[s] == self.inf:
          continue
        if prices[s] + p < tempPrices[d]:
          tempPrices[d] = prices[s] + p
      prices = tempPrices

    return -1 if prices[dst] == self.inf else prices[dst]


def tests():
  n, flights, src, dst, k = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1
  res = Solution().findCheapestPrice(n, flights, src, dst, k)
  print(res)


def driver():
  tests()

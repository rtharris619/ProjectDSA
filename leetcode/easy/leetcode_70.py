class Solution:
  def climbStairs(self, n: int) -> int:
    memo = {}
    def climb(steps: int):
      if steps == n:
        return 1
      if steps > n:
        return 0
      
      if steps in memo:
        return memo[steps]
      
      paths = climb(steps + 1) + climb(steps + 2)
      memo[steps] = paths
      return paths
    
    result = climb(0)
    print(memo)
    return result
  
  def climbStairs2(self, n: int) -> int:
    a, b = 1, 1
    for _ in range(n - 1):
      a, b = a + b, a
    return a
  

def tests():
  n = 5
  # res = Solution().climbStairs(n)
  # print(res)
  print(Solution().climbStairs2(n))


def driver():
  tests()

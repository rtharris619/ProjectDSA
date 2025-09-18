
class Solution:
  def myPow(self, x: float, n: int) -> float:
    def helper(n: int):
      if x == 0:
        return 0
      if n == 0:
        return 1
      result = helper(n // 2)
      result = result * result
      return x * result if n % 2 else result
    result = helper(abs(n))
    return result if n >= 0 else 1 / result


def tests():
  x, n = 2.00000, 10
  print(Solution().myPow(x, n))

def driver():
  tests()

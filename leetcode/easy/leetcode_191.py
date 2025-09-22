class Solution:
  def hammingWeight(self, n: int) -> int:
    result = 0
    while n:
      result += n % 2
      n = n >> 1
    return result
  

def tests():
  n = 11
  print(Solution().hammingWeight(n))
  n = 2147483645
  print(Solution().hammingWeight(n))

def driver():
  tests()

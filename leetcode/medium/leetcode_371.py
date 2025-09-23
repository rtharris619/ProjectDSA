class Solution:
  def getSum(self, a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0:
      carry = (a & b) << 1
      a = a ^ b
      a &= MASK
      carry &= MASK
      b = carry
    return a if a <= MAX_INT else ~(a ^ MASK)


def tests():
  a, b = -12, -8
  print(Solution().getSum(a, b))

def driver():
  tests()

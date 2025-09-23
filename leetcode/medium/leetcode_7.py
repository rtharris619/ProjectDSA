import math

class Solution:
  def reverse(self, x: int) -> int:
    result = 0
    MIN = -214748648
    MAX =  214748647

    while x:
      digit = int(math.fmod(x, 10))
      x = int(x / 10)

      if (result > MAX // 10 or
          (result == MAX // 10 and digit >= MAX % 10)):
        return 0
      if (result < MIN // 10 or
          (result == MIN // 10 and digit <= MIN % 10)):
        return 0

      result = (result * 10) + digit

    return result
  

def tests():
  print(Solution().reverse(123))
  print(Solution().reverse(-123))

def driver():
  tests()

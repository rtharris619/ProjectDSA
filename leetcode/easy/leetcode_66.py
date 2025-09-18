from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    sum = 0
    for i in range(len(digits)):
      sum += digits[i] * (10 ** (len(digits) - i - 1))
    return [int(digit) for digit in str(sum + 1)]
  
def tests():
  digits = [1,2,3]
  print(Solution().plusOne(digits))
  digits = [4,3,2,1]
  print(Solution().plusOne(digits))
  digits = [9]
  print(Solution().plusOne(digits))

def driver():
  tests()

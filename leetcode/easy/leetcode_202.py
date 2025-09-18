class Solution:
  def isHappy(self, n: int) -> bool:
    if n == 1:
      return True
    visited = {}
    sum = n

    while True:
      nums = [int(digit) for digit in str(sum)]
      sum = 0
      for num in nums:
        sum += num * num
      if sum == 1:
        return True
      else:
        if sum in visited:
          return False
        else:
          visited[sum] = visited.get(0, sum)
  
  def isHappy2(self, n: int) -> bool:
    visited = set()
    while n not in visited:
      visited.add(n)
      n = self.sumOfSquares(n)
      if n == 1:
        return True
    return False
  
  def sumOfSquares(self, n: int) -> int:
    result = 0
    while n > 0:
      digit = n % 10
      digit = digit ** 2
      result += digit
      n = n // 10
    return result


def tests():
  n = 19
  print(Solution().isHappy2(n))
  n = 2
  print(Solution().isHappy2(n))

def driver():
  tests()

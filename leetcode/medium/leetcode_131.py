from typing import List


class Solution:
  def partition(self, s: str) -> List[List[str]]:
    result = []
    partition = []

    def backtrack(i: int):
      if i == len(s):
        result.append(partition[:])
        return
      
      for j in range(i, len(s)):
        if self.is_palindrome(s, i, j):
          partition.append(s[i:j+1])
          backtrack(j + 1)
          partition.pop()
          
    backtrack(0)

    return result


  def is_palindrome(self, s: str, L: int, R: int):
    while L < R:
      if s[L] != s[R]:
        return False
      L += 1
      R -= 1
    return True


def tests():
  s = "aab"
  result = Solution().partition(s)
  print(result)


def driver():
  tests()

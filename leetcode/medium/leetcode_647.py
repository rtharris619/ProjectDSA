class Solution:
  def countSubstrings(self, s: str) -> int:
    if len(s) == 1:
      return 1
    
    hashset = set()
    def dfs(start: int, end: int):
      if start < 0 or end >= len(s) or start > end:
        return
      if s[start] != s[end]:
        return
      
      if (start, end) not in hashset:
        hashset.add((start,end))
        dfs(start - 1, end + 1)

    for i in range(len(s)):
      dfs(i, i) # odd length palindromes
      dfs(i, i + 1) # even length palindromes

    return len(hashset)
  
  def counter(self, s: str, i: int, j: int) -> int:
    count = 0
    L, R = i, j
    while L >= 0 and R < len(s) and s[L] == s[R]:
      count +=1
      L -= 1
      R += 1
    return count

  def countSubstrings2(self, s: str) -> int:
    if len(s) == 1:
      return 1
    result = 0
    for i in range(len(s)):
      result += self.counter(s, i, i) # odds
      result += self.counter(s, i, i + 1) # evens

    return result
  
def tests():
  s = "abc"
  res = Solution().countSubstrings2(s)
  print(res)
  s = "aaa"
  res = Solution().countSubstrings2(s)
  print(res)

def driver():
  tests()

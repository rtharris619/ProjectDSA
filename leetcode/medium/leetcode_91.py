class Solution:
  def numDecodings(self, s: str) -> int:
    if s[0] == '0':
      return 0
    
    memo = {}    
    def dfs(i: int):
      if i >= len(s):
        return 1
      
      if s[i] == '0':
        return 0
      
      if i in memo:
        return memo[i]
      
      result = 0
      result += dfs(i + 1)

      if i + 1 < len(s):
        two_digits = int(s[i:i+2])
        if 10 <= two_digits <= 26:
          result += dfs(i + 2)

      memo[i] = result
      return result

    return dfs(0)


def tests():
  s = "226"
  res = Solution().numDecodings(s)
  print(res)

def driver():
  tests()

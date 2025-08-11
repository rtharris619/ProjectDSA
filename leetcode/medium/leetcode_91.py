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
  
  def numDecodings2(self, s: str) -> int:
    dp = {len(s) : 1}

    for i in range(len(s) - 1, -1, -1):
      if s[i] == '0':
        dp[i] = 0
      else:
        dp[i] = dp[i + 1]
    
      if i + 1 < len(s):
        two_digits = int(s[i:i+2])
        if 10 <= two_digits <= 26:
          dp[i] += dp[i + 2]
    print(dp)
    return dp[0]


def tests():
  s = "226"
  res = Solution().numDecodings2(s)
  print(res)

def driver():
  tests()

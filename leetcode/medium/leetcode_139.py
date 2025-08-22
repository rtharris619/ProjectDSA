from typing import List

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
      for word in wordDict:
        if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
          dp[i] = dp[i + len(word)]
        if dp[i]:
          break
    
    return dp[0]


def tests():
  s, wordDict = "leetcode", ["leet","code"]
  res = Solution().wordBreak(s, wordDict)
  print(res)

  s, wordDict = "applepenapple", ["apple","pen"]
  res = Solution().wordBreak(s, wordDict)
  print(res)

  s, wordDict = "catsandog", ["cats","dog","sand","and","cat"]
  res = Solution().wordBreak(s, wordDict)
  print(res)


def driver():
  tests()

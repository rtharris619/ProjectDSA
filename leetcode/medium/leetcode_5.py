class Solution:
  def isPalindrome(self, s: str) -> bool:
    L = 0
    R = len(s) - 1
    while L < R:
      if s[L] != s[R]:
        return False
      L += 1
      R -= 1
    return True
  
  def longestPalindrome(self, s: str) -> str:
    if len(s) == 1:
      return s

    memo = {}
    def dfs(start: int, end: int):
      if start > end:
        return ""
      if start == end:
        return s[start]
      
      if (start, end) in memo:
        return memo[(start, end)]
      
      strToEval = s[start:end + 1]
      if self.isPalindrome(strToEval):
        memo[(start, end)] = strToEval
        return strToEval
      
      option1 = dfs(start + 1, end)
      option2 = dfs(start, end - 1)

      largest = option1 if len(option1) > len(option2) else option2
      memo[(start, end)] = largest
      return largest

    return dfs(0, len(s) - 1)
  
  def longestPalindrome2(self, s: str) -> str:
    if len(s) == 1:
      return s
    
    result = ""
    resultLength = 0

    for i in range(len(s)):
      L, R = i, i
      while L >= 0 and R < len(s) and s[L] == s[R]:
        if (R - L + 1) > resultLength:
          resultLength = (R - L + 1)
          result = s[L:R+1]
        L -= 1
        R += 1

      L, R = i, i + 1
      while L >= 0 and R < len(s) and s[L] == s[R]:
        if (R - L + 1) > resultLength:
          resultLength = (R - L + 1)
          result = s[L:R+1]
        L -= 1
        R += 1

    return result


def tests():
  s = "babad"
  res = Solution().longestPalindrome2(s)
  print(res)
  s = "cbbd"
  res = Solution().longestPalindrome2(s)
  print(res)
  s = "crbidxnkyieminyzchamldzjzglygkfbbyggagwdqdqamzpguppqjfrcewfduwvcmhliahovcwoupwxwhaoiiiguahuqxiqndwxqxweppcbeoasgtucyqlxnxpvtepwretywgjigjjuxsrbwucatffkrqyfkesakglyhpmtewfknevopxljgcttoqonxpdtzbccpyvttuaisrhdauyjyxgquinvqvfvzgusyxuqkyoklwslljbimbgznpvkdxmakqwwveqrpoiabmiegoyzuyoignfcgmqxvpcmldivknulqbpyxjuvyhrzcsgiusdhsogftokekbdynmksyebsnzbxjxfvwamccphzzlzuvotvubqvhmusdtwvlsnbqwqhqcigmlfoupnqcxdyflpgodnoqaqfekhcyxythaiqxzkahfnblyiznlqkbithmhhytzpcbkwicstapygjpjzvrjcombyrmhcusqtslzdyiiyvujnrxvkrwffwxtmdqqrawtvayiskcnpyociwkeopardpjeyuymipekbefbdfuybfvgzfkjtvurfkopatvusticwbtxdtfifgklpmjamiocalcocqwdivyulupammxhdbeazrrktxiyothnvbwwrsocxzxaxmoenigbhvxffddexrwsioqoyovaqvtmkwzupstkgkmvrddzolmuzjnsj"
  res = Solution().longestPalindrome2(s)
  print(res)

def driver():
  tests()

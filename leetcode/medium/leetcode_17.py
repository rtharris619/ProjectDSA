from typing import List


class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    result = []

    hashmap = {}
    hashmap["2"] = "abc"
    hashmap["3"] = "def"
    hashmap["4"] = "ghi"
    hashmap["5"] = "jkl"
    hashmap["6"] = "mno"
    hashmap["7"] = "pqrs"
    hashmap["8"] = "tuv"
    hashmap["9"] = "wxyz"

    def backtrack(i: int, current: str):
      if len(digits) == len(current):
        result.append(current)
        return
      
      for c in hashmap[digits[i]]:
        backtrack(i + 1, current + c)
    
    if digits:
      backtrack(0, "")
    
    return result


  def letterCombinations_2(self, digits: str) -> List[str]:
      result = []

      hashmap = {}
      hashmap["2"] = "abc"
      hashmap["3"] = "def"
      hashmap["4"] = "ghi"
      hashmap["5"] = "jkl"
      hashmap["6"] = "mno"
      hashmap["7"] = "pqrs"
      hashmap["8"] = "tuv"
      hashmap["9"] = "wxyz"

      current = []
      def backtrack(i: int):
        if len(digits) == len(current):
          result.append(''.join(current[:]))
          return
        
        for c in hashmap[digits[i]]:
          current.append(c)
          backtrack(i + 1)
          current.pop()
      
      if digits:
        backtrack(0)
      
      return result

def tests():
  digits = "23"
  result = Solution().letterCombinations_2(digits)
  print(result)


def driver():
  tests()

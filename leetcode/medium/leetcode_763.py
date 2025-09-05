from typing import List

class Solution:
  def partitionLabels(self, s: str) -> List[int]:
    result = []
    lastIndexMap = {}

    for i in range(len(s)):
      lastIndexMap[s[i]] = i

    R, size = 0, 1
    for i in range(len(s)):
      R = max(R, lastIndexMap[s[i]])
      if i == R:
        result.append(size)
        size = 0
      size += 1

    return result
  
def tests():
  s = "ababcbacadefegdehijhklij"
  print(Solution().partitionLabels(s))
  s = "eccbbbbdec"
  print(Solution().partitionLabels(s))

def driver():
  tests()

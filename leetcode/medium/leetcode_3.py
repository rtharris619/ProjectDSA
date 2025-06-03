

def length_of_longest_substring(s: str) -> int:
  myset = set()
  L = 0
  result = 0

  for R in range(len(s)):
    
    while s[R] in myset:
      myset.remove(s[L])
      L += 1

    myset.add(s[R])
    result = max(result, R - L + 1)

  return result


def tests():
  s = "abcabcbb" # a b c a b c b b
  res = length_of_longest_substring(s)
  print(res)

  s = "bbbbb"
  res = length_of_longest_substring(s)
  print(res)

  s = "pwwkew"
  res = length_of_longest_substring(s)
  print(res)


def driver():
  tests()

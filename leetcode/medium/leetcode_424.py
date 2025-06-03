import collections


def character_replacement(s: str, k: int) -> int:
  result = 0
  count = collections.defaultdict(int)
  L = 0

  for R in range(len(s)):
    count[s[R]] += 1
    # window length - most frequent character >= k
    window = R - L + 1
    most_frequent = max(count.values())
    replacements = window - most_frequent
    if replacements <= k:
      result = max(result, window)
    else:
      count[s[L]] -= 1
      L += 1

  return result


def tests():
  s, k = 'ABABBA', 2 # A B A B B A
  res = character_replacement(s, k)
  print(res)
  s, k = 'ABAB', 2
  res = character_replacement(s, k)
  print(res)
  s, k = 'AABABBA', 1
  res = character_replacement(s, k)
  print(res)


def driver():
  tests()

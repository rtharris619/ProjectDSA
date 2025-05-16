
def valid_anagram(s: str, t: str) -> bool:
  
  if len(s) != len(t):
    return False
  
  s_map = {}
  t_map = {}

  for i in range(len(s)):
    s_map[s[i]] = 1 + s_map.get(s[i], 0)
    t_map[t[i]] = 1 + t_map.get(t[i], 0)

  for c in s_map:
    if s_map[c] != t_map.get(c, 0):
      return False
  
  return True


def tests():
  s = "anagram"
  t = "nagaram"
  result = valid_anagram(s, t)
  print(result)

  s = "rat"
  t = "car"
  result = valid_anagram(s, t)
  print(result)


def driver():
  tests()

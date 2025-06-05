

def min_window(s: str, t: str) -> str:
  max_length = 0
  max_pair = ()

  tmap = {}
  window = {}

  for c in t:
    tmap[c] = tmap.get(c, 0) + 1
    window[c] = 0

  need = len(t)
  have = 0

  L = 0
  R = 0
  while L < len(s) - 1 and R < len(s) - 1:
    if s[R] in tmap:
      window[s[R]] += 1
      if window[s[R]] == tmap[s[R]]:
        have += 1

    if have == need:
      if R - L + 1 > max_length:
        max_length = R - L + 1
        max_pair = (L, R)
      L += 1

    R += 1
  
  print(max_length, max_pair)

  if max_pair:
    return s[max_pair[0] : max_pair[1] + 1] 
  else:
    return ''


def tests():
  s = 'ADOBECODEBANC'
  t = 'ABC'
  result = min_window(s, t)
  print(result)
  # result = "BANC"


def driver():
  tests()

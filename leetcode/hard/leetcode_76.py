

def min_window(s: str, t: str) -> str:

  if len(t) > len(s):
    return ''

  min_length = float('infinity')
  min_pair = (-1,-1)

  tmap = {}
  window = {}

  for c in t:
    tmap[c] = tmap.get(c, 0) + 1

  need = len(tmap)
  have = 0

  L = 0

  for R in range(len(s)):
    c = s[R]
    window[c] = window.get(c, 0) + 1

    if c in tmap and window[c] == tmap[c]:
      have += 1

    while have == need:
      if (R - L + 1) < min_length:
        min_length = (R - L + 1)
        min_pair = (L, R)
      
      # pop off from the left of the window (to check for smaller window)
      window[s[L]] -= 1
      if s[L] in tmap and window[s[L]] < tmap[s[L]]:
        have -= 1
      L += 1
  
  L, R = min_pair
  
  return s[L:R+1] if min_length != float('infinity') else ''


def tests():
  s = 'ADOBECODEBANC'
  t = 'ABC'
  result = min_window(s, t)
  print(result)

  s = "aa"
  t = "aa"
  result = min_window(s, t)
  print(result)


def driver():
  tests()

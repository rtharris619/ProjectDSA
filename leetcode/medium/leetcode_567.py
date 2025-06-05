def check_inclusion(s1: str, s2: str) -> bool:
  
  if len(s1) > len(s2):
    return False

  s1count, s2count = [0] * 26, [0] * 26
  for i in range(len(s1)):
    s1count[ord(s1[i]) - ord('a')] += 1
    s2count[ord(s2[i]) - ord('a')] += 1

  matches = 0
  for i in range(26):
    matches += (1 if s1count[i] == s2count[i] else 0)
  
  L = 0
  for R in range(len(s1), len(s2)):
    if matches == 26:
      return True
    
    index = ord(s2[R]) - ord('a')
    s2count[index] += 1
    if s1count[index] == s2count[index]:
      matches += 1
    elif s1count[index] + 1 == s2count[index]:
      matches -= 1

    index = ord(s2[L]) - ord('a')
    s2count[index] -= 1
    if s1count[index] == s2count[index]:
      matches += 1
    elif s1count[index] - 1 == s2count[index]:
      matches -= 1
    
    L += 1

  if matches == 26:
    return True

  return False


def tests():
  s1 = 'abc'
  s2 = 'baxyzabc'
  res = check_inclusion(s1, s2)
  print(res)

  s1 = "ab"
  s2 = "eidbaooo"
  res = check_inclusion(s1, s2)
  print(res)

  s1 = "ab"
  s2 = "eidboaoo"
  res = check_inclusion(s1, s2)
  print(res)


def driver():
  tests()

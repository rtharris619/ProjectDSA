
def is_palindrome(s: str):
  new_s = ''

  for c in s:
    if c.isalnum():
      new_s += c.lower()
 
  j = 0
  for i in range(len(new_s)-1, -1, -1):
    if new_s[i] != new_s[j]:
      return False
    j += 1
        
  return True

def is_palindrome2(s: str):
  new_s = ''

  for c in s:
    if c.isalnum():
      new_s += c.lower()
  
  if new_s != new_s[::-1]:
    return False
  
  return True

def is_palindrome3(s: str):
  left = 0
  right = len(s) - 1

  while left < right:
    while left < right and not s[left].isalnum():
      left += 1

    while left < right and not s[right].isalnum():
      right -= 1

    if s[left].lower() != s[right].lower():
      return False

    left += 1
    right -= 1

  return True


def tests():
  s = "A man, a plan, a canal: Panama"
  out = is_palindrome3(s)
  print(out)
  s = "race a car"
  out = is_palindrome3(s)
  print(out)
  s = " "
  out = is_palindrome3(s)
  print(out)


def driver():
  tests()

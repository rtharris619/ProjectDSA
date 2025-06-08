
def is_valid(s: str) -> bool:

  stack = []
  opening_chars = ['(', '{', '[']

  for i in range(len(s)):
    if s[i] in opening_chars:
      stack.append(s[i])
    else:
      if len(stack) == 0:
        return False
      else:
        item = stack.pop()
        if item == '(' and s[i] != ')':
          return False
        elif item == '[' and s[i] != ']':
          return False
        elif item == '{' and s[i] != '}':
          return False

  return len(stack) == 0


def is_valid2(s: str) -> bool:
  stack = []
  map = {
    ")" : "(",
    "}": "{",
    "]": "["
  }

  for c in s:
    if c in map:
      if stack and stack[-1] == map[c]:
        stack.pop()
      else:
        return False
    else:
      stack.append(c)
  
  return False if stack else True


def tests():
  s = "()[]{}"
  res = is_valid2(s)
  print(res)

  s = "(]"
  res = is_valid2(s)
  print(res)

  s = "([])"
  res = is_valid2(s)
  print(res)

  s = "["
  res = is_valid2(s)
  print(res)

  s = "]"
  res = is_valid2(s)
  print(res)


def driver():
  tests()

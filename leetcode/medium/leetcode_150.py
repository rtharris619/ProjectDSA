from typing import List


def eval_RPN(tokens: List[str]) -> int:

  stack = []
  operators = ["+", "-", "*", "/"]

  for c in tokens:
    if c not in operators:
      stack.append(int(c))
    else:
      b = stack.pop()
      a = stack.pop()
      if c == "+":
        stack.append(a + b)
      elif c == "-":
        stack.append(a - b)
      elif c == "*":
        stack.append(a * b)
      else:
        stack.append(int(a / b))

  return stack[0] if stack else 0


def tests():
  tokens = ["2", "1", "+", "3", "*"]
  res = eval_RPN(tokens)
  print(res)

  tokens = ["4", "13", "5", "/", "+"]
  res = eval_RPN(tokens)
  print(res)

  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
  res = eval_RPN(tokens)
  print(res)


def driver():
  tests()

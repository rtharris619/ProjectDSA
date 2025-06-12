from typing import List

def generate_parenthesis(n: int) -> List[str]:
  stack = []
  result = []  

  def backtrack(open_count: int, closed_count: int):
    if open_count == closed_count == n:
      result.append("".join(stack))
      return

    if open_count < n:
      stack.append('(')
      backtrack(open_count + 1, closed_count)
      stack.pop()
      
    if closed_count < open_count:
      stack.append(')')
      backtrack(open_count, closed_count + 1)
      stack.pop()
  
  backtrack(0, 0)

  return result


def tests():
  res = generate_parenthesis(3)
  print(res)


def driver():
  tests()

from typing import List

def daily_temps(temperatures: List[int]) -> List[int]:
  result = [0] * len(temperatures)
  stack = []

  for i, temp in enumerate(temperatures):
    while stack and temp > stack[-1][0]:
      _, s_index = stack.pop()
      result[s_index] = (i - s_index)
    stack.append([temp, i])
    
  return result


def tests():
  temperatures = [73,74,75,71,69,72,76,73]
  res = daily_temps(temperatures)
  print(res)


def driver():
  tests()

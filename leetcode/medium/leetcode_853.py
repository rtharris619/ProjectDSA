from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]):
  cars = sorted([[p, s] for p, s in zip(position, speed)], reverse=True)
  stack = []

  for car in cars:
    prev_time = stack[-1] if stack else -1
    current_time = (target - car[0]) / car[1] # 3 hours, 2.5 hours, 2.33 hours
    stack.append(current_time)

    if prev_time >= current_time:
      stack.pop()

  return len(stack)


def tests():
  target = 10
  position = [3,5,7]
  speed = [3,2,1]
  res = car_fleet(target, position, speed)
  print(res)

  target = 12
  position = [10,8,0,5,3]
  speed = [2,4,1,1,3]
  res = car_fleet(target, position, speed)
  print(res)

  target = 100
  position = [0,2,4]
  speed = [4,2,1]
  res = car_fleet(target, position, speed)
  print(res)


def driver():
  tests()

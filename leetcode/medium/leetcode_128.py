
def longest_consecutive(nums: list[int]) -> int:
  nums_set = set(nums)
  max_length = 0

  for num in nums_set:
    sub_set = set()

    if num - 1 not in nums_set:
      sub_set.add(num)

      current = num + 1
      while current in nums_set:
        sub_set.add(current)
        current += 1

    if len(sub_set) > max_length:
      max_length = len(sub_set)

  return max_length


def longest_consecutive2(nums: list[int]) -> int:
  nums_set = set(nums)
  max_length = 0

  for num in nums_set:
    if num - 1 not in nums_set:
      length = 0
      while (num + length) in nums_set:
        length += 1
      max_length = max(max_length, length)

  return max_length


def tests():
  nums = [100,4,200,1,3,2]
  result = longest_consecutive2(nums)
  print(result)
  nums = [0,3,7,2,5,8,4,6,0,1]
  result = longest_consecutive2(nums)
  print(result)
  nums = [1,0,1,2]
  result = longest_consecutive2(nums)
  print(result)

def driver():
  tests()

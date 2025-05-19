
def two_sum(nums: list[int], target: int) -> list[int]:
  hashmap = {}

  for i in range(len(nums)):
    difference = target - nums[i]
    if difference in hashmap:
      return [hashmap[difference], i]
    hashmap[nums[i]] = i    

  return []


def two_sum_2(nums: list[int], target: int) -> list[int]:
  prev_map = {}

  for i, n in enumerate(nums):
    diff = target - n
    if diff in prev_map:
      return [prev_map[diff], i]
    prev_map[n] = i


def tests():
  nums = [2,7,11,15]
  target = 9
  result = two_sum(nums, target)
  print(result)


def driver():
  tests()

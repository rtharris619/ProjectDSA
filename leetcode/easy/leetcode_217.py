
def contains_duplicate(nums: list[int]) -> bool:
  hashset = set()

  for num in nums:
    if (num in hashset):
      return True
    hashset.add(num)
  
  return False


def tests():
  ex1 = [1,2,3,1]
  result = contains_duplicate(ex1)
  print(result)

  ex2 = [1,2,3,4]
  result = contains_duplicate(ex2)
  print(result)

  ex3 = [1,1,1,3,3,4,3,2,4,2]
  result = contains_duplicate(ex3)
  print(result)


def driver():
  tests()

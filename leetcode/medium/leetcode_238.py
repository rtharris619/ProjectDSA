
def product_of_array_except_self(nums: list[int]) -> list[int]:
  prefix = [1] * len(nums)
  postfix = [1] * len(nums)
  output = [1] * len(nums)

  for i in range(len(nums)):
    if i > 0:
      prefix[i] = nums[i] * prefix[i-1]
    else:
      prefix[i] = nums[0]

  for i in range(len(nums) - 1, -1, -1):
    if i == len(nums) - 1:
      postfix[i] = nums[len(nums) - 1]
    else:
      postfix[i] = nums[i] * postfix[i+1]

  for i in range(len(nums)):
    if i == 0:
      output[i] = 1 * postfix[i+1]
    elif i == len(nums) - 1:
      output[i] = prefix[i-1] * 1
    else:
      output[i] = prefix[i-1] * postfix[i+1]

  return output

def product_of_array_except_self_2(nums: list[int]) -> list[int]:
  pass


def tests():
  nums = [1,2,3,4]
  result = product_of_array_except_self(nums)
  print(result)

  nums = [-1,1,0,-3,3]
  result = product_of_array_except_self(nums)
  print(result)


def driver():
  tests()

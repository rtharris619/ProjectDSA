class Solution:
  def multiply(self, num1: str, num2: str) -> str:
    if "0" in [num1, num2]:
      return "0"
    
    result = [0] * (len(num1) + len(num2))
    num1, num2 = num1[::-1], num2[::-1]

    for i1 in range(len(num1)):
      for i2 in range(len(num2)):
        digit = int(num1[i1]) * int(num2[i2])
        result[i1 + i2] += digit
        result[i1 + i2 + 1] += (result[i1 + i2] // 10)
        result[i1 + i2] = (result[i1 + i2] % 10)

    result, beginning = result[::-1], 0
    while beginning < len(result) and result[beginning] == 0:
      beginning += 1

    result = map(str, result[beginning:])
    return "".join(result)


def tests():
  num1, num2 = "123", "456"
  print(Solution().multiply(num1, num2))

def driver():
  tests()

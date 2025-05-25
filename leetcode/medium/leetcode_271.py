import re

def encode(strs: list[str]) -> str:
  result = ''
  for string in strs:
    result += str(len(string)) + '$' + string
  return result

def decode(string: str) -> list[str]:
  result = []
  pattern = r'(\d+)\$'

  i = 0
  while i < len(string):
    match = re.match(pattern, string[i:])
    if match:
      length = int(match.group(1))
      start = i + match.end()
      end = start + length
      result.append(string[start:end])
      i = end
    else:
      break
  return result

def decode2(string: str) -> list[str]:
  result = []

  i = 0
  while i < len(string):
    j = i
    while string[j] != '$':
      j += 1
    length = int(string[i:j])
    result.append(string[j + 1 : j + 1 + length])
    i = j + 1 + length

  return result


def tests():
  inp = ["neet","cod$e"]
  encoded = encode(inp)
  print(encoded)
  decoded = decode2(encoded)
  print(decoded)


def driver():
  tests()

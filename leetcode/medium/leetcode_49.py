
from collections import defaultdict


def group_anagrams(words: list[str]):
  result = defaultdict(list) # mapping char count to list of anagrams

  for word in words:
    count = [0] * 26 # a...z

    for c in word:
      count[ord(c) - ord('a')] += 1
    
    result[tuple(count)].append(word) # group all anagrams with this particular count

  return result.values()


def tests():
  ex1 = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
  result = group_anagrams(ex1)
  print(result)  


def driver():
  tests()

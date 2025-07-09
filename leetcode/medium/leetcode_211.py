class WordNode:
  def __init__(self):
    self.children = {}
    self.end = False

class WordDictionary:
  def __init__(self):
    self.root = WordNode()

  def addWord(self, word: str) -> None:
    current = self.root
    for c in word:
      if c not in current.children:
        current.children[c] = WordNode()
      current = current.children[c]
    current.end = True

  def search(self, word: str) -> bool:

    def dfs(j, node):
      current = node
      for i in range(j, len(word)):
        c = word[i]
        if c == '.':
          for child in current.children.values():
            if dfs(i + 1, child):
              return True
          return False
        else:
          if c not in current.children:
            return False
          current = current.children[c]
      return current.end
  
    return dfs(0, self.root)


def tests():
  words = WordDictionary()
  words.addWord("bad")
  words.addWord("dad")
  words.addWord("mad")
  print(words.search("pad"))
  print(words.search("bad"))
  print(words.search(".ad"))


def driver():
  tests()

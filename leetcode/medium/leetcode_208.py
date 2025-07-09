class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    current = self.root
    for c in word:
      if c not in current.children:
        current.children[c] = TrieNode()
      current = current.children[c]
    current.endOfWord = True

  def search(self, word: str) -> bool:
    current = self.root
    for c in word:
      if c not in current.children:
        return False
      current = current.children[c]
    return current.endOfWord

  def startsWith(self, prefix: str) -> bool:
    current = self.root
    for c in prefix:
      if c not in current.children:
        return False
      current = current.children[c]
    return True

  # A challenge for later
  def endsWith(self, postfix: str) -> bool:
    pass

  # Another challenge for later
  def contains(self, text: str) -> bool:
    current = self.root
    if text[0] in current:
      pass


def tests():
  trie = Trie()
  trie.insert("apple")
  print(trie.search("apple"))
  print(trie.search("app"))
  trie.insert("app")
  print(trie.search("app"))


def driver():
  tests()

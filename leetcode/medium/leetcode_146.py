
class Node:
  def __init__(self, key, val):
    self.key, self.val = key, val
    self.prev = self.next = None

class LRUCache:
  def __init__(self, capacity: int):
    self.cap = capacity
    self.cache = {}
    self.LRU, self.MR = Node(0, 0), Node(0, 0)
    self.LRU.next = self.MR
    self.MR.prev = self.LRU

  def remove(self, node: Node):
    prev, next = node.prev, node.next
    prev.next, next.prev = next, prev

  # insert at the rightmost position (MR)
  def insert(self, node: Node):
    prev, next = self.MR.prev, self.MR
    prev.next = next.prev = node
    node.next, node.prev = next, prev

  def get(self, key: int) -> int:
    if key in self.cache:
      self.remove(self.cache[key])
      self.insert(self.cache[key])
      return self.cache[key].val
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.remove(self.cache[key])
    
    self.cache[key] = Node(key, value)
    self.insert(self.cache[key])

    if len(self.cache) > self.cap:
      lru = self.LRU.next
      self.remove(lru)
      del self.cache[lru.key]


def tests():
  lRUCache = LRUCache(2)
  lRUCache.put(1, 1)
  lRUCache.put(2, 2)
  print(lRUCache.get(1))


def driver():
  tests()

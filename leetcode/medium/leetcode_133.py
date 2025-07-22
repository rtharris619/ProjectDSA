from typing import Optional


class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []


class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    clone = {}
    def dfs(node: Node):
      if node in clone:
        return clone[node]
      
      cp = Node(node.val)
      clone[node] = cp
      for neighbor in node.neighbors:
        cp.neighbors.append(dfs(neighbor))
      return cp
    return dfs(node)



def tests():
  node = Node(1, [Node(2, Node(3)), Node(4)])
  result = Solution().cloneGraph(node)
  print(result.val)


def driver():
  tests()

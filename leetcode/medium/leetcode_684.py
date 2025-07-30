from typing import List
import helpers.graph_helper as helper

class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    parents = [i for i in range(len(edges) + 1)]
    ranks = [1] * (len(edges) + 1)
    
    def find(n: int):
      p = parents[n]
      while p != parents[p]:
        parents[p] = parents[parents[p]] # enhancement
        p = parents[p]
      return p
    
    def union(n1: int, n2: int):
      p1, p2 = find(n1), find(n2)
      if p1 == p2:
        return False

      if ranks[p1] > ranks[p2]:
        parents[p2] = p1
        ranks[p1] += ranks[p2]
      else:
        parents[p1] = p2
        ranks[p2] += ranks[p1]
      return True
    
    for n1, n2 in edges:
      if not union(n1, n2):
        return [n1, n2]


def tests():
  edges = [[1,2],[1,3],[2,3]]
  result = Solution().findRedundantConnection(edges)
  print(result)
  # helper.GraphHelper('Redundant Connection').draw_undirected_graph(edges)


def driver():
  tests()

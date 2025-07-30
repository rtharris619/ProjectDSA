from typing import List
import helpers.graph_helper as helper

class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    parents = [i for i in range(n)]
    rank = [1] * n
    
    def find(n1: int) -> int:
      result = n1
      while result != parents[result]:
        parents[result] = parents[parents[result]]
        result = parents[result]
      return result
    
    def union(n1: int, n2: int) -> int:
      p1, p2 = find(n1), find(n2)
      if p1 == p2:
        return 0
      
      if rank[p2] > rank[p1]:
        parents[p1] = p2
        rank[p2] += rank[p1]
      else:
        parents[p2] = p1
        rank[p1] += rank[p2]

      return 1
    
    result = n
    for n1, n2 in edges:
      result -= union(n1, n2)
    return result
  

def tests():
  n, edges = 5, [[0,1], [1,2], [3,4]]
  result = Solution().countComponents(n, edges)
  print(result)
  # helper.GraphHelper('Number of Connected Components in an Undirected Graph').draw_undirected_graph(edges)


def driver():
  tests()

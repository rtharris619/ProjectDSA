from typing import List
import helpers.graph_helper as helper

class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    if not n:
      return True
    
    adjacencies = { i:[] for i in range(n) }
    for n1, n2 in edges:
      adjacencies[n1].append(n2)
      adjacencies[n2].append(n1)

    visited = set()
    def dfs(i: int, prev: int) -> bool:
      if i in visited:
        return False
      
      visited.add(i)
      for j in adjacencies[i]:
        if j == prev:
          continue
        if not dfs(j, i):
          return False
      
      return True
    
    return dfs(0, -1) and n == len(visited)
    

def tests():
  n, edges = 5, [[0,1], [0,2], [0,3], [1,4]]
  res = Solution().validTree(n, edges)
  print(res)

  helper.GraphHelper('Graph Valid Tree').draw_undirected_graph(edges)


def driver():
  tests()

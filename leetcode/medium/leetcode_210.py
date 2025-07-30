from typing import List
import helpers.graph_helper as helper
from collections import defaultdict

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    visited, cycle = set(), set()
    adjacencies = defaultdict(list)
    result = []

    for course, prerequisite in prerequisites:
      adjacencies[course].append(prerequisite)

    def dfs(course: int) -> bool:
      if course in cycle:
        return False
      if course in visited:
        return True
      
      cycle.add(course)
      for prerequisite in adjacencies[course]:
        if not dfs(prerequisite):
          return False
      cycle.remove(course)
      visited.add(course)
      result.append(course)

      return True
    
    for course in range(numCourses):
      if not dfs(course):
        return []
      
    return result


def tests():
  numCourses, prerequisites = 6, [[0, 1], [0, 2], [1, 3], [3, 2], [4, 0], [5, 0]]
  result = Solution().findOrder(numCourses, prerequisites)
  print(result)
  # helper.GraphHelper('Course Schedule II').draw_directed_graph(prerequisites)


def driver():
  tests()

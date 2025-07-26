from typing import List
import helpers.graph_helper as helper
from collections import defaultdict

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adjacencies = defaultdict(list)
    visited = set()

    for course, prerequisite in prerequisites:
      adjacencies[course].append(prerequisite)

    def dfs(course: int) -> bool:
      if course in visited:
        return False
      if adjacencies[course] == []:
        return True
      
      visited.add(course)
      for prerequisite in adjacencies[course]:
        if not dfs(prerequisite): 
          return False
      visited.remove(course)
      adjacencies[course] = []

      return True
      
    for course in range(numCourses):
      if not dfs(course):
        return False

    return True


def tests():
  # numCourses, prerequisites = 2, [[1,0]]
  # Solution().canFinish(numCourses, prerequisites)

  numCourses, prerequisites = 5, [[0,1], [0,2], [1,3], [1,4], [3,4]]
  res = Solution().canFinish(numCourses, prerequisites)
  print(res)

  numCourses, prerequisites = 3, [[0,1], [1,2], [2,0]]
  res = Solution().canFinish(numCourses, prerequisites)
  print(res)
  
  # helper.GraphHelper('Course Schedule').draw_directed_graph(prerequisites)


def driver():
  tests()

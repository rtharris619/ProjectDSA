from structy.helpers.graph_helper import DirectedGraph
from math import inf

# 1. Convert prerequisites to graph edge list.
# 2. Find terminal nodes and mark it distance 0.
# 3. Loop through nodes to find minimum number of semesters required to take all 'n' courses.

def semesters_required(num_courses, prereqs):
    graph = get_edge_list(num_courses, prereqs)
    distances = {}
    for node in graph:
        if len(graph[node]) == 0:
            distances[node] = 1
    for node in graph:
        traversal(graph, node, distances)
    return max(distances.values())

def traversal(graph, node, distances):
    if node in distances:
        return distances[node]
    max_distance = 0
    for neighbor in graph[node]:
        attempt = 1 + traversal(graph, neighbor, distances)
        max_distance = max(max_distance, attempt)
    distances[node] = max_distance
    return max_distance

def get_edge_list(num_courses, prereqs):
    graph = {}
    for course in range(num_courses):
        graph[course] = []

    for edge in prereqs:
        a, b = edge
        graph[a].append(b)
    return graph

def driver():
    num_courses = 6
    prereqs = [
        (1, 2),
        (2, 4),
        (3, 5),
        (0, 5),
    ]
    res = semesters_required(num_courses, prereqs) # -> 3
    print(res)

    num_courses = 7
    prereqs = [
        (4, 3),
        (3, 2),
        (2, 1),
        (1, 0),
        (5, 2),
        (5, 6),
    ]
    res = semesters_required(num_courses, prereqs) # -> 5
    print(res)

    num_courses = 6
    prereqs = [
        (3, 4),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 5),
    ]
    res = semesters_required(num_courses, prereqs) # -> 2
    print(res)

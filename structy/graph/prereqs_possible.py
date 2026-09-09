from structy.helpers.graph_helper import DirectedGraph

def cycle_detected(graph, node, visiting, visited):
    if node in visiting:
        return True
    if node in visited:
        return False

    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detected(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)

    return False

def build_graph(num_courses, prereqs):
    graph = {}
    for i in range(num_courses):
        graph[i] = []

    for prereq in prereqs:
        course1, course2 = prereq
        graph[course1].append(course2)

    return graph

def prereqs_possible(num_courses, prereqs):
    visiting = set()
    visited = set()

    graph = build_graph(num_courses, prereqs)

    for node in graph:
        if cycle_detected(graph, node, visiting, visited):
            return False

    return True

def driver():
    numCourses = 6
    prereqs = [
        (0, 1),
        (2, 3),
        (0, 2),
        (1, 3),
        (4, 5),
    ]

    # graph = DirectedGraph().convert_edges_to_graph(prereqs)
    # DirectedGraph().draw(graph)

    res = prereqs_possible(numCourses, prereqs) # -> True
    print(res)
from structy.helpers.graph_helper import UndirectedGraph

def dfs_rec(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)
    size = 1
    for neighbor in graph[current]:
        size += dfs_rec(graph, neighbor, visited)
    return size

def largest_component(graph):
    largest = 0
    visited = set()

    for node in graph:
        size = dfs_rec(graph, node, visited)
        if size > largest:
            largest = size

    return largest

def driver():
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
    # UndirectedGraph().draw(graph)

    res = largest_component(graph) # -> 4
    print(res)
from structy.helpers.graph_helper import UndirectedGraph
from collections import deque

def dfs_rec(graph: dict, current, visited: set):
    if current in visited:
        return False
    visited.add(current)

    for neighbor in graph[current]:
        dfs_rec(graph, neighbor, visited)
    return True

def dfs(graph: dict, node, visited: set):
    if node  in visited:
        return False
    
    visited.add(node)
    stack = [node]

    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return True

def bfs(graph: dict, node, visited: set):
    if node in visited:
        return False
    visited.add(node)
    queue = deque([node])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return True

def connected_components_count(graph: dict):
    count = 0
    visited = set()

    for node in graph:
        if bfs(graph, node, visited):
            count += 1

    return count

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

    res = connected_components_count(graph)
    print(res)
from structy.helpers.graph_helper import DirectedGraph
from collections import deque

# This algorithm assumes no cycles.

def has_path_rec(graph: dict, src: str, dst: str) -> bool:
    if src == dst:
        return True
    for neighbor in graph[src]:
        if has_path_rec(graph, neighbor, dst):
            return True
    return False

def has_path(graph: dict, src: str, dst: str) -> bool:
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

def driver():
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }

    DirectedGraph().draw(graph)

    res = has_path(graph, 'f', 'k') # True
    print(res)
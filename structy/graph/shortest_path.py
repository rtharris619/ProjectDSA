from structy.helpers.graph_helper import UndirectedGraph
from collections import deque

def shortest_path(edges, node_A: str, node_B: str):
    graph = UndirectedGraph().convert_edges_to_graph(edges)    
    visited = set(node_A)
    queue = deque([(node_A, 0)])
    while queue:
        current, distance = queue.popleft()
        if current == node_B:
            return distance
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                visited.add(neighbor)

    return -1

def driver():
    edges = [
        ['m', 'n'],
        ['n', 'o'],
        ['o', 'p'],
        ['p', 'q'],
        ['t', 'o'],
        ['r', 'q'],
        ['r', 's']
    ]

    # UndirectedGraph().draw_using_edges(edges)
    res = shortest_path(edges, 'm', 's')
    print(res)
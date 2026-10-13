from structy.helpers.graph_helper import DirectedGraph

# Look for terminal nodes first and give them a distance of 0.
# DFS on each node to find distances.

def longest_path(graph):
    distances = {}
    for node in graph:
        if len(node) == 0:
            distances[node] = 0

    for node in graph:
        traversal(graph, node, distances)

    return max(distances.values())

def traversal(graph, node, distances):
    if node in distances:
        return distances[node]
    max_distance = 0
    for neighbor in graph[node]:
        distance = 1 + traversal(graph, neighbor, distances)
        max_distance = max(max_distance, distance)
    distances[node] = max_distance
    return distances[node]

def driver():
    graph = {
        'a': ['c', 'b'],
        'b': ['c'],
        'c': []
    }

    res = longest_path(graph) # -> 2
    print(res)

    graph = {
        'a': ['c', 'b'],
        'b': ['c'],
        'c': [],
        'q': ['r'],
        'r': ['s', 'u', 't'],
        's': ['t'],
        't': ['u'],
        'u': []
    }

    res = longest_path(graph) # -> 4
    print(res)

    graph = {
        'a': ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
        'b': ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
        'c': ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
        'd': ['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
        'e': ['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
        'f': ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
        'g': ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
        'h': ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
        'i': ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
        'j': ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
        'k': ['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
        'l': ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
        'm': ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
        'n': ['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        'o': ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
        'p': ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
        'q': ['r', 's', 't', 'u', 'v', 'w', 'x', 'y'],
        'r': ['s', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        's': ['t', 'u', 'v', 'w', 'x', 'y', 'z'],
        't': ['u', 'v', 'w', 'x', 'y', 'z'],
        'u': ['v', 'w', 'x', 'y', 'z'],
        'v': ['w', 'x', 'y', 'z'],
        'w': ['x', 'y', 'z'],
        'x': ['y', 'z'],
        'y': ['z'],
        'z': []
    }

    # DirectedGraph().draw(graph)

    res = longest_path(graph) # -> 25
    print(res)
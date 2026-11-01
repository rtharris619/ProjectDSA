# Write a function, topological_order, that takes in a dictionary representing the adjacency list for a directed-acyclic graph.
# The function should return a list containing the topological-order of the graph.
# The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence.


def topological_order(graph):
    num_parents = {}
    for parent in graph:
        num_parents[parent] = 0
    for parent in graph:
        for child in graph[parent]:
            num_parents[child] += 1
    ready = [ node for node in num_parents if num_parents[node] == 0 ]
    res = []
    while ready:
        current = ready.pop()
        res.append(current)
        for child in graph[current]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)
    return res
    

def driver():
    res = topological_order({
        "a": ["f"],
        "b": ["d"],
        "c": ["a", "f"],
        "d": ["e"],
        "e": [],
        "f": ["b", "e"],
    }) # -> ['c', 'a', 'f', 'b', 'd', 'e']
    print(res)

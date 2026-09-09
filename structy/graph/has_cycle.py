from structy.helpers.graph_helper import DirectedGraph

###
### Uses the White-Grey-Black Algorithm.
### White is Unexplored, Grey is Visiting, Black is Visited.
###

def dfs(graph: dict, node: str, visiting: set, visited: set):
    if node in visiting:
        return True
    if node in visited:
        return False
    
    visiting.add(node)

    for neighbor in graph[node]:
        if dfs(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)
    
    return False

def has_cycle(graph: dict):
    visiting = set()
    visited = set()

    for node in graph:
        if dfs(graph, node, visiting, visited):
            return True

    return False

def driver():
    graph = {
        "a": ["b"],
        "b": ["c"],
        "c": ["a"],
    }
    # DirectedGraph().draw(graph)
    res = has_cycle(graph) # -> True
    print(res)

    graph = {
        "a": ["b", "c"],
        "b": ["c"],
        "c": ["d"],
        "d": [],
    }
    res = has_cycle(graph) # -> False
    print(res)
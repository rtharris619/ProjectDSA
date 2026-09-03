from structy.helpers.graph_helper import UndirectedGraph, GraphHelper

def has_path(graph: dict, src: str, dst: str, visited: set) -> bool:
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited):
            return True
    return False

def undirected_path(edges: list[tuple], node_A: str, node_B: str):
    graph = GraphHelper().convert_edges_to_graph(edges)
    return has_path(graph, node_A, node_B, set())

def driver():
    edges = [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]

    # UndirectedGraph().draw_using_edges(edges)

    res = undirected_path(edges, 'j', 'm') # -> True
    print(res)

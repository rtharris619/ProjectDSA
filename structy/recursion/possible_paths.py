# Write a function that takes in a graph adjacency list, a source node, and a destination node. 
# The function should return a list containing all possible paths that travel between the source and destination.
# You can assume that the graph is a DAG (directed-acyclic-graph).

from structy.helpers.graph_helper import DirectedGraph

def possible_paths(graph, src, dst):
    return [ path[::-1] for path in traverse(graph, src, dst) ]

# Time: O(n * 2^n)
def traverse(graph, src, dst):
    if src == dst:
        return [[src]]

    paths = []
    for neighbor in graph[src]:
        neighbor_paths = traverse(graph, neighbor, dst)
        for neighbor_path in neighbor_paths:
            # Add the src node to each recursive result. 
            # (Will be reversed later since it should be inserted at the beginning of the path list)
            neighbor_path.append(src)
            paths.append(neighbor_path)

    return paths

def driver():
    graph = {
        "a": ["b", "c", "d"],
        "b": ["d"],
        "c": ["d"],
        "d": []
    }
    # DirectedGraph().draw(graph)
    res = possible_paths(graph, "a", "d") # ->
    # [
    #   ["a", "b", "d"],
    #   ["a", "c", "d"],
    #   ["a", "d"]
    # ]
    print(res)

# Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph.
# The function should return a boolean indicating whether or not it is possible to color nodes of the graph using two colors
# in such a way that adjacent nodes are always different colors.

def can_color(graph):
    coloring = {}
    for node in graph:
        if node not in coloring and not dfs(graph, node, coloring, True):
            return False
    return True

def dfs(graph, node, coloring, current_color):
    if node in coloring:
        return coloring[node] == current_color
    coloring[node] = current_color
    for neighbor in graph[node]:
        if not dfs(graph, neighbor, coloring, not current_color):
            return False
    return True

def driver():
    # Given this graph:
    # x-y-z
    # It is possible to color the nodes by using red for x and z, 
    # then use blue for y. So the answer is True.

    res = can_color({
        "x": ["y"],
        "y": ["x","z"],
        "z": ["y"]
    }) # -> True
    print(res)

    # For example, given this graph:

    #     q
    #    / \
    #   s - r

    # It is not possible to color the nodes without making two 
    # adjacent nodes the same color. So the answer is False.
    res = can_color({
        "q": ["r", "s"],
        "r": ["q", "s"],
        "s": ["r", "q"]
    }) # -> False
    print(res)

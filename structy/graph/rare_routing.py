from structy.helpers.graph_helper import UndirectedGraph

# Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples
# where each tuple represents a direct road that connects a pair of cities.
# The function should return a boolean indicating whether or not there exists a unique route for every pair of cities.
# A route is a sequence of roads that does not visit a city more than once.

# Cities will be numbered 0 to n - 1.
# You can assume that all roads are two-way roads.
# This means if there is a road between A and B, then you can use that road to go from A to B or go from B to A.


def rare_routing(n, roads):
    graph = edge_list_to_adjacency_list(n, roads)
    visited = set()
    valid = dfs(graph, 0, visited, None)
    return valid and len(visited) == n


def dfs(graph, node, visited, last_node):
    if node in visited:
        return False
    visited.add(node)
    for neighbor in graph[node]:
        # nuance: don't backtrack for this algo
        if neighbor != last_node and not dfs(graph, neighbor, visited, node):
            return False
    return True


def edge_list_to_adjacency_list(n: int, roads: list[tuple[int, int]]):
    graph = {}
    for city in range(n):
        graph[city] = []
    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)
    return graph


def driver():

    # For example, given these roads:

    # 0 --- 1
    # | \
    # |  \
    # |   \
    # 2    3

    # There is a unique route for between every pair of cities.
    # So the answer is True.

    # For example, given these roads:

    # 0 --- 1
    # | \
    # |  \
    # |   \
    # 2 -- 3

    # There are two routes that can be used to travel from city 1 to city 2:
    # - first route:  1, 0, 2
    # - second route: 1, 0, 3, 2
    # The answer is False, because routes should be unique.

    res = rare_routing(4, [
        (0, 1),
        (0, 2),
        (0, 3)
    ]) # -> True
    print(res)
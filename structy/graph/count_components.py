# Write a function, count_components, that takes in a number of nodes (n) and a list of edges for an undirected graph.
# In the graph, nodes are labeled from 0 to n - 1. 
# The function should return the number of connected components in the given graph.

# This will be practice for implementing the basic Union-Find algorithm for graphs.
# Watch the approach and walkthrough videos first!


def find(roots: list[int], node: int) -> int:
    if roots[node] == node:
        return node
    return find(roots, roots[node])


def union(roots: list[int], node_a: int, node_b: int):
    root_a = find(roots, node_a)
    root_b = find(roots, node_b)

    if root_a == root_b:
        return

    roots[root_a] = root_b


def count_components(n, edges):
    roots = [i for i in range(n)]
    for edge in edges:
        a, b = edge
        union(roots, a, b)
    count = 0
    for i in range(n):
        if roots[i] == i:
            count += 1
    return count


def driver():
    res = count_components(7, [
        (0, 2),
        (1, 0),
        (4, 3),
        (2, 5),
        (3, 6)
    ]) # -> 2
    print(res)

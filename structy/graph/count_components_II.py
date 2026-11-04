# Let's learn more about union-find algorithm by implementing size and path-compression.
# Watch the approach and walkthrough videos first.
# Write a function, countComponents, that takes in a number of nodes (n) and a list of edges for an undirected graph.
# In the graph, nodes are labeled from 0 to n - 1.
# The function should return the number of connected components in the given graph.

# Solve this by implementing the complete Union-Find algorithm with size and path-compression.


def find(roots, node):
    if roots[node] == node:
        return node
    found = find(roots, roots[node])
    roots[node] = found
    return found


def union(roots, sizes, a, b):
    root_a = find(roots, a)
    root_b = find(roots, b)

    if root_a == root_b:
        return

    if sizes[root_a] >= sizes[root_b]:
        roots[root_b] = root_a
        sizes[root_a] += sizes[root_b]
    else:
        roots[root_a] = root_b
        sizes[root_b] += sizes[root_a]


def count_components(n, edges):
    roots = [ i for i in range(n) ]
    sizes = [ 1 for _ in range(n) ]

    for edge in edges:
        a, b = edge
        union(roots, sizes, a, b)
    count = 0
    for i in range(n):
        if roots[i] == i:
            count +=1
    return count


def driver():
    res = count_components(10, [
        (3, 2),
        (5, 4),
        (4, 3),
        (2, 1),
        (0, 1),
        (8, 9),
        (5, 6),
        (7, 8)
    ]) # -> 2
    print(res)

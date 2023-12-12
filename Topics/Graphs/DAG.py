
def dfs(node, adjacency_list, depths, visited):
    visited[node] = True

    for neighbour in adjacency_list[node]:
        if not visited[neighbour]:
            dfs(neighbour, adjacency_list, depths, visited)

        depths[node] = max(depths[node], 1 + depths[neighbour])


def find_longest_path(adjacency_list, n):
    depths = [0] * (n + 1)

    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, adjacency_list, depths, visited)

    answer = 0

    for i in range(1, n + 1):
        answer = max(answer, depths[i])

    print(answer)


def add_edge(adjacency_list, u, v):
    adjacency_list[u].append(v)


def solve():
    n = 5
    adjacency_list = [[] for i in range(n + 1)]

    add_edge(adjacency_list, 1, 2)
    add_edge(adjacency_list, 1, 3)
    add_edge(adjacency_list, 3, 2)
    add_edge(adjacency_list, 2, 4)
    add_edge(adjacency_list, 3, 4)

    find_longest_path(adjacency_list, n)


def driver():
    solve()

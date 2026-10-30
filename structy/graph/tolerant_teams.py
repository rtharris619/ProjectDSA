from structy.helpers.graph_helper import UndirectedGraph

# Write a function, tolerant_teams, that takes in a list of rivalries as an argument.
# A rivalry is a pair of people who should not be placed on the same team.
# The function should return a boolean indicating whether or not it is possible to separate people into two teams,
# without rivals being on the same team. The two teams formed do not have to be the same size.

def tolerant_teams(rivalries):
    graph = convert_to_graph(rivalries)
    coloring = {}
    for node in graph:
        if node not in coloring and not is_bipartite(graph, node, coloring, False):
            return False
    return True

def is_bipartite(graph, node, coloring, current_color):
    if node in coloring:
        return coloring[node] == current_color
    coloring[node] = current_color
    for neighbor in graph[node]:
        if not is_bipartite(graph, neighbor, coloring, not current_color):
            return False
    return True

def convert_to_graph(edges: list[tuple[str, str]]):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def driver():
    edges = [
        ('philip', 'seb'),
        ('raj', 'nader')
    ]
    res = tolerant_teams(edges) # -> True
    print(res)

    # edges = [
    #     ('philip', 'seb'),
    #     ('raj', 'nader'),
    #     ('raj', 'philip'),
    #     ('seb', 'raj')
    # ]
    # res = tolerant_teams(edges) # -> False

    # edges = [
    #     ('cindy', 'anj'),
    #     ('alex', 'matt'),
    #     ('alex', 'cindy'),
    #     ('anj', 'matt'),
    #     ('brando', 'matt')
    # ]
    # res = tolerant_teams(edges) # -> True
    # # graph = UndirectedGraph()
    # # graph.draw_using_edges(edges)

    # edges = [
    #     ('alex', 'anj'),
    #     ('alex', 'matt'),
    #     ('alex', 'cindy'),
    #     ('anj', 'matt'),
    #     ('brando', 'matt')
    # ]
    # res = tolerant_teams(edges) # -> False
    # print(res)

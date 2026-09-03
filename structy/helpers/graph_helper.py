import networkx as nx
import matplotlib.pyplot as plt

class GraphHelper:
    def convert_edges_to_graph(self, edges):
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

class DirectedGraph:
    def __init__(self):
        self.G = nx.DiGraph()

    def draw(self, graph: dict):
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                self.G.add_edge(node, neighbor)
        nx.draw(
            self.G,
            with_labels=True,
            node_size=2000,
            font_size=12,
            arrows=True
        )
        plt.show()

class UndirectedGraph:
    def __init__(self):
        self.G = nx.Graph()

    def draw(self, graph: dict):
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                self.G.add_edge(node, neighbor)
        self._plot()

    def draw_using_edges(self, edges: list[tuple]):
        self.G.add_edges_from(edges)
        self._plot()
        
    def _plot(self):
        nx.draw(
            self.G,
            with_labels=True,
            node_size=2000,
            font_size=12,
            arrows=True
        )
        plt.show()
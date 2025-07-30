import networkx as nx
import matplotlib.pyplot as plt
from typing import List


class GraphHelper:
  def __init__(self, title: str):
    self.title = title

  def _plot_undirected_graph(self, G: nx.Graph):
    pos = nx.spring_layout(G)

    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=700)

    # Draw the edges (no arrows for undirected)
    nx.draw_networkx_edges(
        G, 
        pos, 
        edge_color='gray', 
        width=2
    )

    # Draw the labels (node numbers)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    # Display the plot
    plt.title(self.title)
    plt.axis('off')  # Turn off the axis
    plt.show()


  def _plot_directed_graph(self, G: nx.DiGraph):
    pos = nx.spring_layout(G)

    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)

    # Draw the edges
    nx.draw_networkx_edges(
      G, 
      pos, 
      edge_color='gray', 
      arrowstyle='-|>',     
      arrowsize=20,
      min_source_margin=13,
      min_target_margin=13    
    )

    # Draw the labels (node numbers)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

    # Display the plot
    plt.title(self.title)
    plt.axis('off') # Turn off the axis
    plt.show()


  def draw_directed_graph(self, edges: List[List[int]]):
    G = nx.DiGraph()

    for edge in edges:
      G.add_edge(edge[0], edge[1])

    self._plot_directed_graph(G)


  def draw_undirected_graph(self, edges: List[List[int]]):
    G = nx.Graph()

    for edge in edges:
        G.add_edge(edge[0], edge[1])

    self._plot_undirected_graph(G)


# def draw_adjacency_list_test():
#   graph_adj_list = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'E'],
#     'D': ['B'],
#     'E': ['C']    
#   }
#   G = nx.DiGraph()
#   for node, neighbors in graph_adj_list.items():
#     G.add_node(node)
#     for neighbor in neighbors:
#         G.add_edge(node, neighbor)
  
#   plt.figure(figsize=(8, 6)) # Optional: Adjust figure size
#   nx.draw_networkx(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
#   plt.title("Graph Visualization from Adjacency List")
#   plt.axis('off') # Hide axes
#   plt.show()


# def draw_from_edges_test():
#   edges = [(1, 2), (2, 3), (1, 3), (3, 4), (4, 1)]
#   # G = nx.Graph()  # For an undirected graph
#   G = nx.DiGraph() # For a directed graph
#   G.add_edges_from(edges)

#   # Choose a layout algorithm (e.g., spring_layout for a more natural look)
#   pos = nx.spring_layout(G)

#   # Draw the nodes
#   nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)

#   # Draw the edges
#   nx.draw_networkx_edges(
#     G, 
#     pos, 
#     edge_color='gray', 
#     arrowstyle='-|>',     
#     arrowsize=20,
#     min_source_margin=13,
#     min_target_margin=13    
#   )

#   # Draw the labels (node numbers)
#   nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

#   # Display the plot
#   plt.title("Graph from Adjacency List (Edges)")
#   plt.axis('off') # Turn off the axis
#   plt.show()



import networkx as nx
import matplotlib.pyplot as plt

graph = nx.fast_gnp_random_graph(10, 0.3, seed=42, directed=False)
nx.draw(graph, with_labels=True)
plt.show()
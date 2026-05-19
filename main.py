import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.components import is_connected
from networkx.algorithms.euler import is_eulerian, eulerian_circuit

graph = nx.fast_gnp_random_graph(10, 0.3, directed=False)
number_edges = graph.number_of_edges() #Stores the number of edges of the generated graph
bol_connected = is_connected(graph) #checks if the generated graph is connected
bol_euler = is_eulerian(graph) #checks if the generated graph contains an Euler's Circuit

if bol_connected:
    print(f"The generated 10 vertices graph is connected and contains {number_edges} edges")
else:
    print(f"The generated 10 vertices graph is unconnected")

if bol_euler:
    try:
        eulerian_circuit_walk = list(nx.eulerian_circuit(graph))
        if eulerian_circuit_walk:
            print("The generated 10 vertices graph contains an Euler's Circuit through the following sequence: ",eulerian_circuit_walk)
    except nx.exception.NetworkXError:
        pass
else:
    print(f"The generated 10 vertices graph does not contain an Eulerian circuit")

try:
    eulerian_circuit_walk = list(nx.eulerian_circuit(graph))
    if eulerian_circuit_walk:
        print("The generated 10 vertices Euler Circuit graph has the following edge traversal sequence: ", eulerian_circuit_walk)
except nx.exception.NetworkXError:
    pass



nx.draw(graph, with_labels=True)
plt.show()
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.components import is_connected
from networkx.algorithms.euler import is_eulerian, eulerian_circuit

graph = nx.fast_gnp_random_graph(10, 0.3, directed=False)
number_edges = graph.number_of_edges() #Stores the number of edges of the generated graph
bol_connected = is_connected(graph) #checks if the generated graph is connected
bol_euler = is_eulerian(graph) #checks if the generated graph contains an Euler's Circuit
# Display degrees of vertices
print("\nDegrees of vertices:")

for node, degree in graph.degree():
    print(f"Vertex {node}: Degree {degree}")

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

#  Probability Estimation

trials = 10000

connected_graphs = 0
eulerian_connected_graphs = 0

for i in range(trials):

    random_graph = nx.fast_gnp_random_graph(10, 0.3)


    if nx.is_connected(random_graph):

        connected_graphs += 1


        if nx.is_eulerian(random_graph):

            eulerian_connected_graphs += 1


if connected_graphs > 0:

    probability = eulerian_connected_graphs / connected_graphs

    print("\n----- Probability Estimation -----")
    print("Total random graphs generated:", trials)
    print("Connected graphs:", connected_graphs)
    print("Connected Eulerian graphs:", eulerian_connected_graphs)

    print(
        "Estimated Probability of Euler Circuit GIVEN connected graph:",
        probability
    )

nx.draw(graph, with_labels=True)
plt.show()

# Graph generator

The graph generator is a python script that generates a random undirected graph, analyzes its structural properties to check whether it contains a Euler circuit or not. it then produces an output of the graph in the terminal if it has a Euler circuit. The script also calculates the empirical probability that a random connected graph is also Eulerian and displays that value.  

## Overview

The script uses the NetworkX library to:

Generate a random undirected graph with 10 vertices using the Erdős–Rényi G(n, p) model.

Count the number of edges in the generated graph.

Check whether the graph is connected.

Check whether the graph contains an Eulerian circuit.

If an Eulerian circuit exists, print the edge traversal sequence.

run 10000 trials to estimate the conditional probability that a random connected graph on 10 vertices with edge probability 0.3 is Eulerian.

Display a visualization of the generated graph using matplotlib.

Because the graph is generated randomly on each run, the output will differ between executions. 
Some runs will produce a connected and/or Eulerian graph, while others will not.

## Requirements

Python 3.7 or later

NetworkX

Matplotlib

Install the dependencies with:

pip install networkx matplotlib

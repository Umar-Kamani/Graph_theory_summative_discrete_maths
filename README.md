# Graph generator and Analyser

This is a small Python script that generates a random undirected graph and analyzes two of its structural properties: 
whether it is connected and whether it contains an Euler circuit or not. it then produces an output of the graph in the terminal if it has a Euler circuit.

## Overview

The script uses the NetworkX library to:

Generate a random undirected graph with 10 vertices using the Erdős–Rényi G(n, p) model.

Count the number of edges in the generated graph.

Check whether the graph is connected.

Check whether the graph contains an Eulerian circuit.

If an Eulerian circuit exists, print the edge traversal sequence.

Because the graph is generated randomly on each run, the output will differ between executions. 
Some runs will produce a connected and/or Eulerian graph, while others will not.

## Requirements

Python 3.7 or later

NetworkX

Matplotlib

Install the dependencies with:

pip install networkx matplotlib

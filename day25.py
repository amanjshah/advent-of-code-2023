import math
import os
import networkx as nx


def createGraph():
    data = [line.split(": ") for line in open(os.path.join("input-data-2023", "23-25.txt")).read().strip().split("\n")]
    graph = nx.Graph()
    for node, connectedNodes in data:
        for connectedNode in (connectedNodes.split()):
            graph.add_edge(node, connectedNode)
            graph.add_edge(connectedNode, node)
    return graph


def getResult():
    graph = createGraph()
    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    return math.prod(map(len, nx.connected_components(graph)))


print(getResult())

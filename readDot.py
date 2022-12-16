# reading the road map

import networkx as nx
from graph import *
print(nx.nx_agraph.read_dot("roadmap.dot"))

graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])
# graph.py

from typing import NamedTuple
import networkx as nx
from queues import Queue, Stack
from collections import deque
from math import inf as infinity
from queues import MutableMinHeap, Queue, Stack


class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )

    def load_graph(filename, node_factory):
        graph = nx.nx_agraph.read_dot(filename)
        nodes = {
            name: node_factory(attributes)
            for name, attributes in graph.nodes(data=True)
        }
        return nodes, nx.Graph(
            (nodes[name1], nodes[name2], weights)
            for name1, name2, weights in graph.edges(data=True)
        )

    def breadth_first_traverse(graph, source):
        queue = Queue(source)
        visited = {source}
        while queue:
            yield node := queue.dequeue()
            neighbors = list(graph.neighbors(node))
            if order_by:
                neighbors.sort(key=order_by)
            for neighbor in neighbor:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

    def breadth_first_search(graph, source, predicate, order_by=None):
        return search(depth_first_traverse, graph, source, predicate, order_by)

    def search(traverse, graph, source, predicate, order_by=None):
    for node in traverse(graph, source, order_by):
        if predicate(node):
            return node

    def dijkstra_shortest_path(graph, source, destination, weight_factory):
        previous = {}
        visited = set()

        unvisited = MutableMinHeap()
        for node in graph.nodes:
            unvisited[node] = infinity
        unvisited[source] = 0

        while unvisited:
            visited.add(node := unvisited.dequeue())
            for neighbor, weights in graph[node].items():
                if neighbor not in visited:
                    weight = weight_factory(weights)
                    new_distance = unvisited[node] + weight
                    if new_distance < unvisited[neighbor]:
                        unvisited[neighbor] = new_distance
                        previous[neighbor] = node
                    
        return retrace(previous, source, destination)



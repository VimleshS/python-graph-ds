from queue import Queue
from adjacencyset import *


def sort_topology(graph):
    queue = Queue()
    in_degree_map = {}

    for v in range(graph.numVertices):
        in_degree_map[v] = graph.get_indegree(v)
        if in_degree_map[v] == 0:
            queue.put(v)

    sorted = []
    while not queue.empty():
        v = queue.get()
        sorted.append(v)

        for _v in graph.get_adjacent_vertices(v):
            in_degree_map[_v] = in_degree_map[_v] - 1
            if in_degree_map[_v] == 0:
                queue.put(_v)

    if len(sorted) != graph.numVertices:
        raise ValueError("Graph is a cyclic")
    print(sorted)


a = AdjacencyGraphSet(9, True)
a.add_edge(0,1)
a.add_edge(1,2)
a.add_edge(2,7)
a.add_edge(2,4)
a.add_edge(2,3)
a.add_edge(1,5) 
a.add_edge(5,6)
a.add_edge(3,6)
a.add_edge(3,4)
a.add_edge(6,8)

sort_topology(a)




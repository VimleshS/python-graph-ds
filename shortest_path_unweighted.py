from queue import Queue
from adjacencyset import *


def distance_table(graph, start_node):
    queue = Queue()

    distance_table_map = {}
    for v in range(graph.numVertices):
        distance_table_map[v] = (None,None)

    distance_table_map[start_node] = (0, None)
    queue.put(start_node)

    while not queue.empty():
        vertex = queue.get()
        vertex_distance = distance_table_map[vertex][0]

        for v in graph.get_adjacent_vertices(vertex):
            if distance_table_map[v][0] is None:
                distance_table_map[v] = (vertex_distance + 1, vertex)
                queue.put(v)

    return distance_table_map


# Backtracking.. uses stack(simulated using list and always prepend)
def get_shortest_path(distance_table, source, destination):
    path = [destination]

    prev_vertex = distance_table[destination][1]
    while prev_vertex is not None and prev_vertex is not source:
        path = [prev_vertex] + path
        prev_vertex = distance_table[prev_vertex][1]

    if prev_vertex is None:
        print("There is no path from %d to %d " % (source, destination))
    else:
        path = [source] + path
        print(path)


a = AdjacencyGraphSet(5,True)
a.add_edge(0,1)
a.add_edge(0,2)
a.add_edge(1,3)
a.add_edge(2,4)
a.add_edge(4,1)
a.add_edge(1,3)

n = distance_table(a, 2)
print(n)
get_shortest_path(n, 2, 3)


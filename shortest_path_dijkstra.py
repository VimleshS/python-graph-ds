import priority_queue
from adjacencymatrix import *

def build_distance_table(graph, source):

    distance_table = {}
    for v in range(graph.numVertices):
        distance_table[v] = (None, None)

    distance_table[source] = (0, source)

    # Node with the lowest value has the highest priority
    _priority_queue = priority_queue.priority_dict()

    _priority_queue[source] = 0
    while len(_priority_queue.keys()) > 0:
        cur_vertex = _priority_queue.pop_smallest()
        cur_distance = distance_table[cur_vertex][0]

        for neighbour in graph.get_adjacent_vertices(cur_vertex):
            distance = cur_distance + graph.get_edge_weight(cur_vertex, neighbour)

            neighbour_distance = distance_table[neighbour][0]
            if neighbour_distance is None or neighbour_distance > distance:
                distance_table[neighbour] = (distance, cur_vertex)
                _priority_queue[neighbour] = distance

    return  distance_table

def shortest_path(graph, source, destination):
    distance_table = build_distance_table(graph, source)

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


#works with directed and undirected

a = AdjacencyMatrixGraph(8,False)
a.add_edge(0,1,1)
a.add_edge(1,2,2)
a.add_edge(1,3,6)
a.add_edge(2,3,2)
a.add_edge(1,4,3)
a.add_edge(3,5,1)
a.add_edge(5,4,5)
a.add_edge(3,6,1)
a.add_edge(6,7,1)
a.add_edge(0,7,8)

shortest_path(a,0,6)
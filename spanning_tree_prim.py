from adjacencymatrix import *
import priority_queue

def spanning_tree(graph, source):
    distance_table = {}
    
    for v in range(graph.numVertices):
        distance_table[v] = (None, None)

    distance_table[source] = (0, source)

    _priority_queue = priority_queue.priority_dict()
    _priority_queue[source] = 0

    visited_vertices = set()
    spanning_tree = set()

    while len(_priority_queue.keys()):
        vertex = _priority_queue.pop_smallest()

        if vertex in visited_vertices:
            continue
        visited_vertices.add(vertex)

        if vertex != source:
            last_vertex = distance_table[vertex][1]
            spanning_tree.add('%s -> %s' % (last_vertex, vertex))
        
        for neighbour in graph.get_adjacent_vertices(vertex):
            # do not sum up the previous distances.
            distance = graph.get_edge_weight(vertex, neighbour)
            neighbour_distance = distance_table[neighbour][0]

            if neighbour_distance is None or neighbour_distance > distance:
                distance_table[neighbour]=(distance, vertex)
                _priority_queue[neighbour] = distance
    
    for edge in spanning_tree:
        print(edge)


# Works with undirected.
a = AdjacencyMatrixGraph(8,False)
a.add_edge(0,1,1)
a.add_edge(1,2,2)
a.add_edge(1,3,2)
a.add_edge(2,3,2)
a.add_edge(1,4,3)
a.add_edge(3,5,1)
a.add_edge(5,4,3)
a.add_edge(3,6,1)
a.add_edge(6,7,1)
a.add_edge(7,0,1)

spanning_tree(a,1)        
            
        


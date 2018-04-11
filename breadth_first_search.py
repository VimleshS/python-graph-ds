from queue import Queue
from adjacencymatrix import *


def bfs(graph, start_vertex):
     queue = Queue()
     queue.put(start_vertex)

     visited = np.zeros(graph.numVertices)
     while not queue.empty():
         vertex = queue.get()

         if visited[vertex] == 1:
             continue

         print("visit: ", vertex)
         visited[vertex] = 1
         for v in graph.get_adjacent_vertices(vertex):
             if visited[v] != 1:
                 queue.put(v)




def dfs(graph, start_vertex):
    visited = np.zeros(graph.numVertices)
    recurse_node(graph,visited,start_vertex)

def recurse_node(graph, visited, cur_node):
    if visited[cur_node] ==1:
        return

    visited[cur_node] = 1
    print("Visit: ", cur_node)
    for v in graph.get_adjacent_vertices(cur_node):
        recurse_node(graph, visited, v)



a = AdjacencyMatrixGraph(9, True)

a.add_edge(0,1)
a.add_edge(1,2)
a.add_edge(2,7)
a.add_edge(2,4)
a.add_edge(2,3)
a.add_edge(1,5)
a.add_edge(5,6)
a.add_edge(6,3)
a.add_edge(3,4)
a.add_edge(6,8)

# bfs(a,2)
dfs(a,0)



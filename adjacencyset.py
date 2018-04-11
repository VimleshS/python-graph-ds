import abc
import numpy as np

class Graph(abc.ABC):
    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed
    
    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass
    
class Node():
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self,v):
        if self.vertexId == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" % (v))
        self.adjacency_set.add(v)
    
    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)

class AdjacencyGraphSet(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyGraphSet, self).__init__(numVertices, directed)
        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        self.vertex_list[v1].add_edge(v2)
        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1 
        return indegree
    
    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "---->", v)


# a = AdjacencyGraphSet(4, False)
# a.add_edge(0,1)
# a.add_edge(0,2)
# a.add_edge(2,3)
#
# for i in range(4):
#     print("Adjancent to ", i, a.get_adjacent_vertices(i))
#
# for i in range(4):
#     print("Indegree ", i, a.get_indegree(i))
#
# for i in range(4):
#     for j in a.get_adjacent_vertices(i):
#         print("Edge Weight", i, " ", j, " " , a.get_edge_weight(i,j))
#
# a.display()
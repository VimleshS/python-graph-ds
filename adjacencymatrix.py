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
    

class AdjacencyMatrixGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        self.matrix = np.zeros((numVertices,numVertices))
    
    def add_edge(self, v1, v2, weight =1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of range" % (v1, v2))
        if weight<0:
            raise ValueError("Weight cannot be less than 1")
            
        self.matrix[v1][v2] = weight
        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        adj_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adj_vertices.append(i)
        return adj_vertices

    def get_indegree(self, v):
        if v >= self.numVertices:
            raise ValueError("Vertices %d is out of range" % (v))
        indices = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indices = indices + 1
        return indices

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "---->", v)


# a = AdjacencyMatrixGraph(4, False)
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

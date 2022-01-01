
import numpy as np
import pandas as pd

class Graph:
    def __init__(self, vertices:list = [], directed:bool = True, initialWeight = np.NAN):
        self.isDirectedGraph = directed
        self.adjacencyMatrix = pd.DataFrame(initialWeight, columns = vertices, index = vertices)

    # Adds a vertex by appending a row and column to the underlying dataframe
    def AddVertex(self, vertexName):
        self.adjacencyMatrix[vertexName] = np.NAN
        self.adjacencyMatrix = self.adjacencyMatrix.append(pd.Series(name = vertexName))
    
    # Deletes a vertex by removing its row and column from the underlying dataframe
    def DeleteVertex(self, vertexName):
        self.adjacencyMatrix = self.adjacencyMatrix.drop(vertexName)
        del self.adjacencyMatrix[vertexName]

    # Sets the weight of an edge
    # NOTE: There is nothing that prevents the user from assigning a weight to an edge traveling to and from the same node
        # This is deliberate in case there is a cost of staying at a node
    def AssignEdgeWeight(self, startNode, endNode, weight):
        self.adjacencyMatrix.at[startNode, endNode] = weight
        if not self.isDirectedGraph:
            self.adjacencyMatrix.at[endNode, startNode] = weight

    # Dijkstra's algorithm for shortest paths
        # Adapting the algorithm from https://brilliant.org/wiki/dijkstras-short-path-finder/
    def DijkstraShortestPaths(self):
        # A tie between vertex names and indices
        vertices = list(enumerate(self.adjacencyMatrix.columns))
        hashishedVertices = {k: v for v, k in vertices} # Gives me O(1) relationship between keynames and numeric indices
        # Numpyfy the dataframe
        numpyAdjMat = self.adjacencyMatrix.to_numpy()
        # Helpful Numbers
        numVertices = len(hashishedVertices)
        maxWeight = np.max(numpyAdjMat)
        foundIndicator = maxWeight + 1

        # Storage arrays
        shortestFound = np.zeros(numVertices) # 0 for false, maxWeight + 1 for true
        shortestDistanceToVertex = np.full(numVertices, np.inf) # Initialize all to infinity (except the first but stay tuned)
        shortestDistanceToVertex[0] = self.adjacencyMatrix[vertices[0][1]][vertices[0][1]]

        while np.min(shortestFound) < foundIndicator:
            # Get the index of the vertex with the lowest weight for which we haven't found the shortest path
            minDex = np.argmin(shortestFound + shortestDistanceToVertex)
            shortestFound[minDex] = foundIndicator # Effectively "pops" the vertex from the tobeprocessed stack

            potentialShortests = numpyAdjMat[minDex] + shortestFound + shortestDistanceToVertex[minDex]
            shortestDistanceToVertex = np.minimum(potentialShortests, shortestDistanceToVertex)
        
        # Pretty it up a bit. Pair each vertex name with the shortest path to get there.
        Solution = {}
        for k in hashishedVertices:
            Solution[k] = shortestDistanceToVertex[hashishedVertices[k]]

        return Solution
    
    # Good ole ToString
    def __str__(self):
        return self.adjacencyMatrix.to_string()

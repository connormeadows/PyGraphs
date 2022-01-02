# Implementing the graph structure and its functions. An exhibitionary test. 
import Graph as g
import random as rand

# A helper so that formatting is consistent
def ExhibitPrint(thingToPrint, label = None):
    print()
    if label:
        print(label)
    print(thingToPrint)

# Arbitrary indices
arbitraryIndices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

# Constructing with the arbitrary vertices
exampleGraphDirected = g.Graph(arbitraryIndices, initialWeight = 1)
exampleGraphUndirected = g.Graph(arbitraryIndices, directed = False)

# Adding a vertex
exampleGraphDirected.AddVertex('Z')
ExhibitPrint(exampleGraphDirected, label = "Added vertex Z")

# Deleting the vertex we just added
exampleGraphDirected.DeleteVertex('Z')
ExhibitPrint(exampleGraphDirected, label = "Deleted vertex Z")

# Assign the weight between B and C for both our directed graph
exampleGraphDirected.AssignEdgeWeight(arbitraryIndices[2], arbitraryIndices[3], 2)
# and our undirected graph
exampleGraphUndirected.AssignEdgeWeight(arbitraryIndices[2], arbitraryIndices[3], 2)
# Go ahead and print those and see what's up
ExhibitPrint(exampleGraphDirected, label = "Directed graph weight assignment")
ExhibitPrint(exampleGraphUndirected, label = "Undirected graph weight assignment")

# Now I'll randomize the weights for the directed graph to play with the cooler functions
for i in range(1000 * len(arbitraryIndices)):
    # Pick a random start and end
    startVert = rand.choice(arbitraryIndices)
    endVert = rand.choice(arbitraryIndices)
    # Give it a random weight from [1,50]
        # For readers unfamiliar with the notation, using brackets means the range of possible values includes the start and end values
    exampleGraphDirected.AssignEdgeWeight(startVert, endVert, rand.randint(1,500))

ExhibitPrint(exampleGraphDirected, label = "Assigned random weights to directed graph")

shortestPathWeights = exampleGraphDirected.DijkstraShortestPaths()
ExhibitPrint(shortestPathWeights, label = "Shortest paths to each vertex")
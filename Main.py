from Graph import Graph

theGraph = Graph()

theGraph.addVertex('A') # 0
theGraph.addVertex('B') # 1
theGraph.addVertex('C') # 2
theGraph.addVertex('D') # 3
theGraph.addVertex('E') # 4
theGraph.addVertex('F') # 5
theGraph.addVertex('G') # 6

theGraph.addEdge(0, 2, 14)
theGraph.addEdge(0, 1, 12)

theGraph.addEdge(1, 2, 9)
theGraph.addEdge(1, 3, 38)

theGraph.addEdge(2, 4, 7)
theGraph.addEdge(2, 3, 24)

theGraph.addEdge(3, 6, 9)

theGraph.addEdge(4, 3, 13)
theGraph.addEdge(4, 6, 29)
theGraph.addEdge(4, 5, 9)

#theGraph.getAdjUnvisitedVertex(0)
print(theGraph.ucs(0, 3))
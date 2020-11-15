from Graph import Graph

theGraph = Graph()

theGraph.addVertex("A") 
theGraph.addVertex('B') 
theGraph.addVertex('C')
theGraph.addVertex('D')
theGraph.addVertex('E')
theGraph.addVertex('F')
theGraph.addVertex('G')
theGraph.addVertex('H')

theGraph.addEdge(0, 0)
theGraph.addEdge(0, 1)
theGraph.addEdge(0, 2)

theGraph.addEdge(1, 1)
theGraph.addEdge(1, 0)
theGraph.addEdge(1, 4)

theGraph.addEdge(2, 2)
theGraph.addEdge(2, 3)

theGraph.addEdge(3, 3)
theGraph.addEdge(3, 2)
theGraph.addEdge(3, 7)

theGraph.addEdge(4, 4)
theGraph.addEdge(4, 5)
theGraph.addEdge(4, 6)

theGraph.addEdge(5, 5)
theGraph.addEdge(5, 4)

theGraph.addEdge(6, 6)

theGraph.addEdge(7, 7)

theGraph.showAdjMat()


theGraph.bfs()
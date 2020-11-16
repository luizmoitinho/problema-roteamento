from Graph import Graph

theGraph = Graph()

theGraph.addVertex("A") # 0
theGraph.addVertex('B') # 1
theGraph.addVertex('C') # 2
theGraph.addVertex('D') # 3
theGraph.addVertex('E') # 4
theGraph.addVertex('F') # 5
theGraph.addVertex('G') # 6

theGraph.addEdge(0, 1, 7)
theGraph.addEdge(0, 2, 8)

theGraph.addEdge(1, 0, 7)
theGraph.addEdge(1, 4, 16)
theGraph.addEdge(1, 4, 3)

theGraph.addEdge(2, 0, 8)
theGraph.addEdge(2, 3, 2)
theGraph.addEdge(2, 3, 12)

theGraph.addEdge(3, 1, 3)
theGraph.addEdge(3, 2, 2)
theGraph.addEdge(3, 4, 14)
theGraph.addEdge(3, 5, 21)

theGraph.addEdge(4, 1, 16)
theGraph.addEdge(4, 3, 14)
theGraph.addEdge(4, 6, 17)

theGraph.addEdge(5, 2, 12)
theGraph.addEdge(5, 3, 21)
theGraph.addEdge(5, 6, 13)

theGraph.addEdge(6, 5, 13)
theGraph.addEdge(6, 4, 17)
theGraph.addEdge(4, 6, 17)

theGraph.showAdjMat()


theGraph.bfs()
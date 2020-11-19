
from src.Router import Router

theGraph = Router()

theGraph.addAccess('A') # 0
theGraph.addAccess('B') # 1
theGraph.addAccess('C') # 2
theGraph.addAccess('D') # 3
theGraph.addAccess('E') # 4
theGraph.addAccess('F') # 5
theGraph.addAccess('G') # 6

theGraph.addLink(0, 2, 14)
theGraph.addLink(0, 1, 12)

theGraph.addLink(1, 2, 9)
theGraph.addLink(1, 3, 38)

theGraph.addLink(2, 4, 7)
theGraph.addLink(2, 3, 24)

theGraph.addLink(3, 6, 9)

theGraph.addLink(4, 3, 13)
theGraph.addLink(4, 6, 29)
theGraph.addLink(4, 5, 9)

#theGraph.getAdjUnvisitedVertex(0)
print(theGraph.ucs(0, 5))
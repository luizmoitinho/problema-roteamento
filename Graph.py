import numpy
from Queue import Queue
from Vertex import Vertex

class Graph:

  def __init__(self):
    self.MAX_VERTS = 7
    self.vertexList =  []
    self.nVerts = 0  
    self.queue = Queue()

  def addVertex(self, label):
    self.vertexList.append(Vertex(label))
    self.nVerts = self.nVerts + 1

  def addEdge(self, startVertex, endVertex, weight):
    self.vertexList[startVertex].edges.append([endVertex, weight])
    self.vertexList[endVertex].edges.append([startVertex, weight])

  def getFather(self, v):
    return self.vertexList[v].edges[0][0]
  
  def displayEdges(self): 
    for i in self.vertexList:
      print("Vertices de", i.label)
      edges = i.edges
      for j in edges:
        print("-> ", j[0], "com", j[1])

  def displayVertice(self,v):
    print(self.vertexList[v].label,end=" ")

  def searchPath(self,initialState,node):
    path = []
    path.append(node)
    nodeFather = self.getFather(node) 
    while( nodeFather != initialState and self.vertexList[nodeFather].wasVisited):
      path.append(nodeFather)
      nodeFather = self.getFather(nodeFather)
    path.append(nodeFather)
    return path

  def ucs(self, nodeStart, nodeGoal):
    initialState = nodeStart
    path = []
    self.vertexList[initialState].wasVisited = True
   
    for i in self.vertexList[initialState].edges:
      self.queue.insert((i[0], i[1]), i[1])

    reachedGoal = False
    cumulativeWeight = -1
    currentNode = initialState
    while(not self.queue.isEmpty()):
      if(currentNode == nodeGoal):
        cumulativeWeight = nodeWeight
        path =  self.searchPath(initialState,currentNode)
        break
      else:
        currentNode, nodeWeight = self.queue.remove()

        self.vertexList[currentNode].wasVisited = True
        for i in self.vertexList[currentNode].edges:
          if(not self.vertexList[i[0]].wasVisited):
            cumulativeCost = i[1] + nodeWeight
            self.queue.insert((i[0], cumulativeCost), cumulativeCost)

    return path
  pass




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
  
  def displayEdges(self): 
    for i in self.vertexList:
      print("Vertices de", i.label)
      edges = i.edges
      for j in edges:
        print("-> ", j[0], "com", j[1])

  def displayVertice(self,v):
    print(self.vertexList[v].label,end=" ")

  def ucs(self, nodeStart, nodeGoal):
    initialState = nodeStart

    self.vertexList[initialState].wasVisited = True
    self.displayVertice(initialState)

    for i in self.vertexList[initialState].edges:
      self.queue.insert((i[0], i[1]), i[1])

    reachedGoal = False
    cumulativeWeight = -1

    while(not self.queue.isEmpty()):
      currentNode, nodeWeight = self.queue.remove()
      self.displayVertice(currentNode)
      self.vertexList[currentNode].wasVisited = True
      if(currentNode == nodeGoal):
        reachedGoal = True
        cumulativeWeight = nodeWeight
        print("Chegou?")
        break
      else:
        for i in self.vertexList[currentNode].edges:
          if(not self.vertexList[i[0]].wasVisited):
            cumulativeCost = i[1] + nodeWeight
            self.queue.insert((i[0], cumulativeCost), cumulativeCost)
    
    print(cumulativeWeight)
  pass
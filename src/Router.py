import numpy
from .Queue import Queue
from .Vertex import Vertex

class Router:

  def __init__(self):
    self.MAX_VERTS = 7
    self.vertexList =  []
    self.nVerts = 0  
    self.queue = Queue()

  def addAccess(self, label):
    self.vertexList.append(Vertex(label))
    self.nVerts = self.nVerts + 1

  def addLink(self, startAccess, endAccess, weight):
    self.vertexList[startAccess].edges.append([endAccess, weight])
    self.vertexList[endAccess].edges.append([startAccess, weight])

  def getFather(self, v):
    return self.vertexList[v].edges[0][0]
  
  def displayLinks(self): 
    for i in self.vertexList:
      print("Vertices de", i.label)
      edges = i.edges
      for j in edges:
        print("-> ", j[0], "com", j[1])

  def displayVertice(self,v):
    print(self.vertexList[v].label,end=" ")

  def searchPath(self,initialAccess,node):
    path = []
    path.insert(0,node)
    nodeFather = self.getFather(node) 
    while( nodeFather != initialAccess and self.vertexList[nodeFather].wasVisited):
      path.insert(0,nodeFather)
      nodeFather = self.getFather(nodeFather)
    path.insert(0,nodeFather)
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
      currentNode, nodeWeight = self.queue.remove()
      if(currentNode == nodeGoal):
        cumulativeWeight = nodeWeight
        path =  self.searchPath(initialState,currentNode)
        break
      else:
        self.vertexList[currentNode].wasVisited = True
        for i in self.vertexList[currentNode].edges:
          if(not self.vertexList[i[0]].wasVisited):
            cumulativeCost = i[1] + nodeWeight
            self.queue.insert((i[0], cumulativeCost), cumulativeCost)

    return path
  pass




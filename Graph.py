import numpy
from Stack import Stack
from Queue import Queue
from Vertex import Vertex


class Graph:

  def __init__(self):
    self.MAX_VERTS = 8
    self.vertexList =  []
    self.adjMat = numpy.zeros((self.MAX_VERTS,self.MAX_VERTS), dtype = numpy.int64)
    self.costs = numpy.zeros((self.MAX_VERTS,self.MAX_VERTS), dtype = numpy.int64)
    self.nVerts = 0  
    self.queue = Queue()

  def addVertex(self, label):
    self.vertexList.append(Vertex(label))
    self.nVerts = self.nVerts + 1

  def addEdge(self, start,end,cost,digrafo = None):
    self.adjMat[start][end] = 1
    self.costs[start][end] = cost

    if(digrafo != None):
      self.adjMat[end][start] = 1
      self.costs[end][start] = coat
    
  def displayVertice(self,v):
    print(self.vertexList[v].label)

  def getAdjUnvisitedVertex(self, v):
    for j in range(self.nVerts):
      if(self.adjMat[v][j] == 1 and self.vertexList[j].wasVisited == False):
        return j

    return -1

  def showAdjMat(self):

    for i in range(self.MAX_VERTS):
      print("%10d"%(i),end="")
    print("")
    for i in range(self.MAX_VERTS):
      print(i,end="    ")
      for j in range(self.MAX_VERTS):
        print("[%2d,%2d]"%(self.adjMat[i][j],self.costs[i][j]),end="   ")
      print("")
  
  def bfs(self):
    initialState = 0;
    print("Estado inicial é %c" %(self.vertexList[initialState].label))
    self.vertexList[initialState].wasVisited = True
    self.displayVertice(initialState)
    self.queue.insert(initialState)

    v2 = 0
    while(not self.queue.isEmpty()):
      v1 = self.queue.remove()
      v2 = self.getAdjUnvisitedVertex(v1)
      while(v2 != -1):
        self.vertexList[v2].wasVisited = True
        self.displayVertice(v2)
        self.queue.insert(v2)

        v2 = self.getAdjUnvisitedVertex(v1)

  pass
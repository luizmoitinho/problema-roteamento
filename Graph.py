import numpy
from Stack import Stack
from Queue import Queue
from Vertex import Vertex


class Graph:

  def __init__(self):
    self.MAX_VERTS = 8
    self.vertexList =  []
    self.adjMat = numpy.zeros((self.MAX_VERTS,self.MAX_VERTS), dtype = numpy.int64)
    self.nVerts = 0  
    self.queue = Queue()

  def addVertex(self, label):
    self.vertexList.append(Vertex(label))
    self.nVerts = self.nVerts + 1

  def addEdge(self, start,end):
    self.adjMat[start][end] = 1
    self.adjMat[end][start] = 1
    
  def displayVertice(self,v):
    print(self.vertexList[v].label)

  def getAdjUnvisitedVertex(self, v):
    for j in range(self.nVerts):
      if(self.adjMat[v][j] == 1 and self.vertexList[j].wasVisited == False):
        return j

    return -1

  def showAdjMat(self):
    print(end="   ")
    for i in range(self.MAX_VERTS):
      print(i,end=" ")
    print("")
    for i in range(self.MAX_VERTS):
      print(i,end="  ")
      for j in range(self.MAX_VERTS):
        print(self.adjMat[i][j],end=" ")
      print("")
  
  
  pass
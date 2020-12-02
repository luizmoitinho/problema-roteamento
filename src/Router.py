
from .Queue import Queue
from .Vertex import Vertex

class Router:

  def __init__(self):
    self.vertexList = []
    self.queue = Queue()

  def addAccess(self, label):
    self.vertexList.append(Vertex(label))

  def addLink(self, startAccess, endAccess, weight):
    self.vertexList[startAccess].edges.append([endAccess, weight])
    self.vertexList[endAccess].edges.append([startAccess, weight])

  def displayLinks(self): 
    for i in self.vertexList:
      print("Vertices de", i.label)
      edges = i.edges
      for j in edges:
        print("-> ", j[0], "com", j[1])

  def displayVertice(self,v):
    print(self.vertexList[v].label,end=" ")

  def ucs(self, nodeStart, nodeGoal):
    for i in self.vertexList:
      i.wasVisited = False
    self.queue.flush()

    initialState = nodeStart
    self.vertexList[initialState].wasVisited = True
    for i in self.vertexList[initialState].edges:
      self.queue.insert((i[0], i[1], [self.vertexList[nodeStart].label]), i[1])

    cumulativeWeight = -1

    while(not self.queue.isEmpty()):
      currentNode, nodeWeight, path = self.queue.remove()
      if(currentNode == nodeGoal):
        path = path + [self.vertexList[currentNode].label]
        cumulativeWeight = nodeWeight
        return path, cumulativeWeight
      else:
        self.vertexList[currentNode].wasVisited = True
        for i in self.vertexList[currentNode].edges:
          if(not self.vertexList[i[0]].wasVisited):
            cumulativeCost = i[1] + nodeWeight
            self.queue.insert((i[0], cumulativeCost, path + [self.vertexList[currentNode].label]), cumulativeCost)
    return path, cumulativeWeight
  pass



    



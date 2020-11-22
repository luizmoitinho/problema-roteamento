
class Vertex:

  def __init__(self, label):
    self.label = label
    self.edges = []
    self.wasVisited = False
    self.parent = -1
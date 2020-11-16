
class List:
  
  def __init__(self):
    self.SIZE = 6
    self.listArray = [self.SIZE]
    self.front = 0
    self.end = 0

  def insert(self, element):
    if()
  
  def remove(self):
    temp = self.queueArray[self.front]
    self.front = self.front + 1
    if(self.front == self.SIZE):
      self.front = 0
    return temp

  
  def binarySearch(self, target):
    left, right = 0
    while(esquerda <= direita):
      middle = (left+right)//2
      if(self.listArray[middle] == item):
        return middle
      elif(self.listArray[middle]>item):
        right = middle + 1
      else:
        left = middle + 1
    return -1 


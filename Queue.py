
class Queue:
  
  def __init__(self):
    self.SIZE = 7
    self.queueArray = [self.SIZE]
    self.front = 0
    self.rear = -1

  def insert(self, element):
    if(self.rear ==  self.SIZE-1):
      self.rear = -1
    self.rear =  self.rear + 1
    self.queueArray.append(element)
  
  def remove(self):
    self.front = self.front + 1
    temp = self.queueArray[self.front]
    if(self.front == self.SIZE):
      self.front = 0
    return temp

  def isEmpty(self):
    return (self.rear+1 == self.front) or (self.front + self.SIZE - 1 == self.rear)
  

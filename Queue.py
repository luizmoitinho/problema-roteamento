
class Queue:
  
  def __init__(self):
    self.SIZE = 8
    self.queueArray = [self.SIZE]
    self.front = 0
    self.rear = -1


  def insert(self, element):
    if(rear ==  self.SIZE-1):
      rear = -1
    self.rear =  self.rear + 1
    self.queueArray[self.rear] = element
  
  def remove(self):
    temp = self.queueArray[self.front]
    self.front = self.front + 1
    if(self.front == self.SIZE):
      self.front = 0
    return temp

  def isEmpty(self):
    return (self.rear+1 == self.front) or (self.front + self.SIZE - 1 == self.rear)
  

import heapq

class Queue:
  
  def __init__(self):
    self.queueArray = []

  def insert(self, item, priority):
    heapq.heappush(self.queueArray, (priority, item))

  def remove(self):
    return heapq.heappop(self.queueArray)[-1]

  def isEmpty(self):
    return len(self.queueArray) == 0

  def flush(self):
    self.queueArray = []
  
  def print(self):
    print(self.queueArray)

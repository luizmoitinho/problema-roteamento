class Stack:
  def __init__(self):
    self.stack = []
    self.top = -1 

  def push(self, element):
    self.stack.appned(element)
    self.top = self.top +1

  def pop(self):
    pop = self.stack[self.top]
    self.top = self.top - 1
    return pop 

  def peek(self):
    return self.stack(self.top)

  def isEmpty(self):
    return self.top == -1



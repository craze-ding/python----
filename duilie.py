class Queue:
    def __init__(self):
        self.items=[] 
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.item.pop()
    def isEmpty(self):
        return self.item==[]
    def size(self):
        return len(self.item)
from pythonds.basic.queue import Queue
q=Queue()
print(q.isEmpty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.isEmpty())
q.enqueue(8.4)
print(q.dequeue())
print(q.dequeue())
print(q.size())
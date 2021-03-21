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
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 5:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
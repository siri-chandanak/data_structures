class Queue:
    def __init__(self):
        self.queue=[]
        self.size=0

    def insert(self, x:int): 
        self.size+=1
        self.queue.append(x)
    
    def dequeue(self) -> int:
        self.size-=1 
        return self.queue.pop(0)
    
    def peek(self) -> int:
        return self.queue[0]
    
    def length(self) -> int:
        return self.size

q = Queue()
for i in range(5):
    q.insert(i)
print("Size:",q.length())
print("Last element:",q.peek())
print("Dequeue:",q.dequeue())
print("Dequeue:",q.dequeue())
print("Dequeue:",q.dequeue())
q.insert(10)
print("Last Element:",q.peek())

class Stack:
    def __init__(self):
        self.stack=[]

    def insert(self, x:int): 
        self.stack.append(x)
    
    def pop(self) -> int: 
        return self.stack.pop(-1)
    
    def peek(self) -> int:
        return self.stack[-1]

stk1 = Stack()
for i in range(5):
    stk1.insert(i)
print("Last element: ",stk1.peek())
print("Pop:",stk1.pop())
print("Pop:",stk1.pop())
print("Pop:",stk1.pop())
stk1.insert(10)
print("Last Element:",stk1.peek())

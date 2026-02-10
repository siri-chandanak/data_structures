class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
    
class Heap:
    def __init__(self):
        self.root=None
    def heapify(self,inorder_list):
        
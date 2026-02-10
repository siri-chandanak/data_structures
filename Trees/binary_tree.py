

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
    
class BinaryTree:
    def __init__(self):
        self.root=None

    def insert_it(self,x):   # Iteration
        # Recursion
        # self.root=self.insert(self.root,x)
        new_node=Node(x)
        if(self.root==None):
            self.root=new_node
            return
        temp=self.root
        while True:
            if(x>temp.data):
                if(temp.right==None):
                    temp.right=new_node
                    return
                temp=temp.right
            else:
                if(temp.left==None):
                    temp.left=new_node
                    return
                temp=temp.left

    def insert(self,node,x):
        if(node==None):
            return Node(x)
        if(x>node.data):
            node.right=self.insert(node.right,x)
        else:
            node.left=self.insert(node.left,x)
        return node
    
    
    def search_it(self,x):
        # Recursion
        # return self.search(self.root,x)
        temp=self.root
        while(temp!=None):
            if(temp.data==x):
                return True
            elif(x>temp.data):
                temp=temp.right
            else:
                temp=temp.left 
        return False
       
    def search(self,node,x):
        if(node.data==x):
            return True
        if(x>node.data and node.right!=None):
            return self.search(node.right,x)
        if(node.left!=None):
            return self.search(node.left,x)
        return False
    
    def check_successor(self):
        n=self.get_successor(self.root) # 50
        print(n.data)
        n=self.get_successor(self.root.left) # 10
        print(n.data)
        n=self.get_successor(self.root.right) # 60
        print(n.data)
        n=self.get_successor(self.root.right.right) # 70
        print(n.data)

    def check_predecessor(self):
        n=self.get_predecessor(self.root) # 50
        print(n.data)
        n=self.get_predecessor(self.root.left) # 10
        print(n)
        n=self.get_predecessor(self.root.right) # 60
        print(n.data)
        n=self.get_predecessor(self.root.right.right) # 70
        print(n.data)
        
    def get_successor(self, node):
        if node.right==None:
            return None
        node=node.right
        while(node.left):
            node=node.left
        return node
    
    def get_predecessor(self,node):
        if node.left==None:
            return None
        node=node.left
        while(node.right):
            node=node.right
        return node
    def traversal(self):
        print("Pre-order Iteration: ",end=" ")
        self.preorder_iteration(self.root)
        print()
        print("Pre-order Recursion: ",end=" ")
        self.preorder_recursion(self.root)
        print()
        print("In-order Iteration: ",end=" ")
        self.inorder_iteration(self.root)
        print()
        print("In-order Recursion: ",end=" ")
        self.inorder_recursion(self.root)
        print()
        print("Post-order Iteration: ",end=" ")
        self.postorder_iteration(self.root)
        print()
        print("Post-order Recursion: ",end=" ")
        self.postorder_recursion(self.root)
        print()
    def preorder_iteration(self,node):
        if node==None:
            return
        stk=[node]
        while(stk):
            n=stk.pop()
            print(n.data,end=" ")
            if(n.right):
                stk.append(n.right)
            if(n.left):
                stk.append(n.left)
    
    def preorder_recursion(self,node):
        if node==None:
            return
        print(node.data,end=" ")
        self.preorder_recursion(node.left)
        self.preorder_recursion(node.right)

    def inorder_iteration(self,node):
        if node==None:
            return
        stk=[]
        temp = node
        while(True):
            while(temp):
                stk.append(temp)
                temp=temp.left
            if(not stk):
                return
            n=stk.pop()
            print(n.data,end=" ")
            temp=n.right

    def inorder_recursion(self,node):
        if node==None:
            return
        self.inorder_recursion(node.left)
        print(node.data,end=" ")
        self.inorder_recursion(node.right)

    def postorder_iteration(self,node):
        if node==None:
            return
        stk=[]
        visited=None
        temp = node
        while(temp or stk):
            if(temp):
                stk.append(temp)
                temp=temp.left
            else:
                n=stk[-1]
                if n.right and visited!=n.right:
                    temp=n.right
                else:   
                    print(n.data,end=" ")
                    visited=stk.pop()

    def postorder_recursion(self,node):
        if node==None:
            return
        self.postorder_recursion(node.left)
        self.postorder_recursion(node.right)
        print(node.data,end=" ")

    def delete(self, x):
        if(not self.search(self.root,x)):
            print("Element not found")
            return
        curr=None
        temp=self.root
        while(1):
            if temp.data==x:
                break
            elif(temp.data>x):
                curr=temp
                temp=temp.left
            else:
                curr=temp
                temp=temp.right
        if(temp.left==None and temp.right==None):
            if(curr==None):
                self.root=None
            elif(curr.left==temp):
                curr.left=None
            elif(curr.right==temp):
                curr.right=None
        elif(temp.left==None or temp.right==None):
            if(temp.left==None):
                temp=temp.right
            else:
                temp=temp.left
        else:
            p=self.get_predecessor(temp)
            p.data,temp.data=p.data,temp.data
            self.delete(x)

bt = BinaryTree()

bt.insert_it(50)
bt.insert_it(10)
bt.insert_it(30)
bt.insert_it(60)
bt.insert_it(70)
bt.insert_it(55)
bt.insert_it(53)
bt.insert_it(58)
bt.insert_it(63)
bt.insert_it(75)
bt.insert_it(61)
bt.insert_it(64)
bt.insert_it(62)


print(bt.search_it(55))
print(bt.search_it(80))

bt.check_successor()
print()
bt.check_predecessor()


bt.traversal()

bt.delete(75)
bt.delete(62)

bt.traversal()
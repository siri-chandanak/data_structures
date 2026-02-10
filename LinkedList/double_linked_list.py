'''
Insertion: O(1)
Deletion: O(n)
Search: O(n)
Traversal: O(n)
Space: O(n)

Time complexity to delete a known node : O(1)

Can use hash map, to get nodes
{10: node1, 20: node2, 30: node3,...}

'''

class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insert(self, x):
        new_node=Node(x)
        self.size+=1
        if not self.head:
            self.head=self.tail=new_node
            return
        '''  
        #if we don't have tail
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        new_node.prev=temp
        temp.next=new_node
        '''
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node

    def deletion(self, x):
        current=self.head
        while(current and current.data!=x):
            current=current.next
        if(not current):
            print("Element",x,"not fount in list")
            return
        if(current.prev==None):  # Delete first node
            self.head=self.head.next
            self.head.prev = None
            if(not self.head):
                self.tail=None
        elif current==self.tail: #Delete last node
            self.tail=current.prev
            self.tail.next=None
        else:
            current.prev.next=current.next
            current.next.prev = current.prev
        self.size-=1
        '''
        # If no tail
        if(current.prev==None):  # Delete first node
            self.head=self.head.next
        else:
            current.prev.next=current.next
        '''

    def delete_at_position(self,pos):
        if(self.size < pos or pos < 1):
            print("Invalid position")
            return
        current=self.head
        for i in range(pos-1):
            current=current.next
        if(current.prev==None):  # Delete first node
            self.head=self.head.next
            self.head.prev = None
            if(not self.head):
                self.tail=None
        elif current==self.tail: #Delete last node
            self.tail=current.prev
            self.tail.next=None
        else:
            current.prev.next=current.next
            current.next.prev = current.prev
        self.size-=1
        '''
        # If no tail
        if(not prev):  # Delete first node
            self.head=self.head.next
        else:
            prev.next=current.next
        '''


    def traversal(self):
        temp=self.head
        for i in range(self.size):
            print(temp.data,end=" ")
            temp=temp.next
        print()
        
    def search(self,x):
        temp=self.head
        for i in range(self.size):
            if(temp.data==x):
                return True
            temp=temp.next
        return False
    
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

ll.traversal()        # 10 20 30 40

ll.deletion(20)
ll.traversal()        # 10 30 40

ll.delete_at_position(3)
ll.traversal()        # 10 30

print(ll.search(30)) # True
print(ll.search(50)) # False

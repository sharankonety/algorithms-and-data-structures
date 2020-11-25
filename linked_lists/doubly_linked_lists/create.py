# Inserting in a doubly linked list.
class Node:
    def __init__(self,data=None):
        self.pre = None
        self.data = data
        self.next = None
class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.pre =  None
            self.tail.next = None
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
            self.tail.next = None
def display(head):
    n = head
    while n:
        print(n.data,end="-->")
        n = n.next
a = Doubly_linked_list()
a_nodes = [1,2,3,4,5]
for x in a_nodes:
    a.insert(x)
display(a.head)
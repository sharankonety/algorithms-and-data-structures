# Implementing a stack using linked list
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.head is None:
            print("stack underflow")
        temp = self.head
        temp = temp.next
        self.head = temp
def display(head):
    while head:
        print(head.data,end="-->")
        head = head.next
    print("/0")
a = Linked_list()
a_nodes = [1,2,3,4,5]
for x in a_nodes:
    a.push(x)
display(a.head)
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
display(a.head)
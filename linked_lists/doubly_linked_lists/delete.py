# program to delete node 
class Node:
    def __init__(self,data=None):
        self.prev = None
        self.data = data
        self.next = None
class Doubly_linked_list:
    def  __init__(self):
        self.head = None
        self.tail = None
    def insert(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.prev = None
            self.tail.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = None
            self.tail = new_node
    def delete_node(self,key):
        temp = self.head
        if temp.data == key:
            temp = temp.next
            temp.prev.next = None
            temp.prev = None
            self.head = temp
            return
        while temp:
            if temp.data != key:
                temp = temp.next
            else:
                if temp.next:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                else:
                    temp.prev.next = None
                    temp = None
                return

def display(head):
    while head:
        print(head.data,end="-->")
        head = head.next
a = Doubly_linked_list()
a_nodes = [1,2,3,4,5]
for x in a_nodes:
    a.insert(x)
a.delete_node(3)
display(a.head)
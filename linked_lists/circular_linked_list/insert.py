# inseerting in a circular linked list
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Circular_linked_list:
    def __init__(self):
        self.head = None
    def display(self):
        print_val = self.head
        print(print_val.data,end="-->")
        print_val = print_val.next
        while print_val != self.head:
            print(print_val.data,end="-->")
            print_val = print_val.next
    def insert_at(self,pre,new_data):
        new_node = Node(new_data)
        new_node.next = pre.next
        pre.next = new_node
a = Circular_linked_list()
a.head = Node(1)
e2 = Node(2)
e3 = Node(3)
a.head.next = e2
e2.next = e3
e3.next = a.head
# a.display()
a.insert_at(e3,4)
a.display()
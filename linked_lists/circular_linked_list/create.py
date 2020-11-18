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
        while print_val != None:
            print(print_val.data,end="-->")
            print_val = print_val.next
a = Circular_linked_list()
a.head = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
a.head.next = e2
e2.next = e3
e3.next = e4
e4.next = a.head
a.display()

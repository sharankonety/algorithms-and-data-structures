class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def Print_list(self):
        print_val = self.head
        while print_val:
            print(print_val.data,end="-->")
            print_val = print_val.next
        print("/0")
list = Linked_list()
list.head = Node(5)
e2 = Node(6)
e3 = Node(8)
list.head.next = e2
e2.next = e3
list.Print_list()

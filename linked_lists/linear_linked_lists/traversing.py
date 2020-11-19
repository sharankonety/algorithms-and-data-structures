# Traversing in a linked list
class Node:
    def __init__(self,data=None,next_val=None):
        self.data = data
        self.next_val = next_val
class linked_list:
    def __init__(self,head_val=None):
        self.head_val = head_val
    
    def print_list(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next_val
list = linked_list()
list.head_val = Node("First name")
e2 = Node("Middle name")
e3 = Node("Last name")

list.head_val.next_val = e2
e2.next_val = e3
list.print_list()

# addition of elements in a linkes list
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next=next
class Linked_list:
    def __init__(self,head = None):
        self.head = head
    def print_list(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next
    def add_list(self):
        add = 0
        temp = self.head
        while temp is not None:
            add += temp.data
            temp = temp.next
        print(add)
list = Linked_list()
list.head = Node(21)
e2 = Node(21)
list.head.next=e2
list.print_list()
list.add_list()
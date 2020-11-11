# check if the linked list is sorted or not
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def print_list(self):
        print_val = self.head
        while print_val:
            print(print_val.data,end="-->")
            print_val = print_val.next
        print("/0")
    def is_sorted(self):
        x = 0
        temp = self.head
        while temp:
            if temp.data<x:
                print("List is not sorted")
                return
            else:
                x = temp.data
                temp = temp.next
        print("list sorted")
list = Linked_list()
list.head = Node(5)
e2 = Node(1)
e3 = Node(8)
list.head.next = e2
e2.next = e3
list.print_list()
list.is_sorted()


# Reversing a linked list(by reversing the links)
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def print_list(self):
        print_val = self.head
        while print_val:
            print(print_val.data,end='-->')
            print_val = print_val.next
        print("/0")
    # function to reverse a linked list
    # we take 2 slidingg pointers alng with the head node and traverse through the linked list with three pointers until
    # p is not none. parallelly we asssign q's next to r (reversing the links) snd finally we assign q as the head node
    def reverse_list(self):
        p = self.head
        q = None
        r = None
        while p:
            r = q
            q = p
            p = p.next
            q.next = r
        self.head = q
list = linked_list()
list.head = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
list.head.next = e2
e2.next = e3
e3.next = e4
list.print_list()
list.reverse_list()
list.print_list()
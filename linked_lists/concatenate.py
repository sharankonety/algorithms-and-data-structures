# concatinating two linked lists
# to concatinate two lists we first need two linked lists. so first we create two linked lists.
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
        self.second_head = None
    # fucntion to print first linked list
    def print_list(self):
        print_val = self.head
        while print_val:
            print(print_val.data,end="-->")
            print_val = print_val.next
        print("/0")
    # function to print the secong linked list
    def print_list1(self):
        print_val = self.second_head
        while print_val:
            print(print_val.data,end="-->")
            print_val = print_val.next
        print("/0")
    # function to concatinate both the linked lists
    # to concatinate, we first assign head of first linked list to a temporary variable and when the next of temp variable
    # is not none we keep traversing through the linked list when it is none we assign temp's next to head of second linked list
    def concatinate(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.second_head
list = Linked_list()
list.head = Node(1)
e2 = Node(2)
e3 = Node(3)
list.head.next = e2
e2.next = e3
list.second_head = Node(4)
a1 = Node(5)
a2 = Node(6)
list.second_head.next = a1
a1.next = a2
list.print_list()
list.print_list1()
list.concatinate()
list.print_list()

# Insert a node at specified index position
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def list_print(self):
        print_val = self.head
        while print_val:
            print(print_val.data)
            print_val = print_val.next
    def list_count(self):
        count = 0 
        x = self.head
        while x:
            count += 1
            x = x.next
        return count
    # Function to insert a node at specific index
    def insert_at_index(self,index,data):
        #  access the variable count from the count_list function. to check if the given index is valid or not
        count = self.list_count()
        if (index<0 or index>count):
            return
        # usually we insert a node at a specific index by accessing the next pointer of the previous node
        # so here we have two methods 1.inserting at the head of the linked list 2. inserting else where in linked list.
        new_node = Node(data)
        n = self.head
        # insert at head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        # while iterating till the index, also traverse through the linked list using the next pointer
        # and when the loop breaks assign the next of previous node to the next of new_node and the next of previous node the new_node
        else:
            for i in range(0,index-1):
                n = n.next
            new_node.next = n.next
            n.next = new_node
list = Linked_list()
# list.head = Node(1)
# e2 = Node(2)
# e3 = Node(3)
# e4 = Node(5)
# list.head.next = e2
# e2.next = e3
# e3.next = e4
list.insert_at_index(0,4)
list.list_print()
# list.list_count()
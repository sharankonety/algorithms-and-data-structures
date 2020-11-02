# Inserting a node at the beginning of the linked list
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
            print(print_val.data, end = " ")
            print_val = print_val.next_val
    def at_beginning(self,New_data):
        # assigning the New_data in the Node class to a new_node
        New_node = Node(New_data)
        # to enter a new value at the beginning we have to assign the previous head value
        # as the next value of new_node
        New_node.next_val = self.head_val
        # as a new node is being inserted at the beginning of the linked list
        # assign the new_node to the head
        self.head_val = New_node
list = linked_list()
list.head_val = Node(".")
e2 = Node("Sai")
e3 = Node("Sharan")
list.head_val.next_val = e2
e2.next_val = e3
list.at_beginning("Konety")
list.print_list()
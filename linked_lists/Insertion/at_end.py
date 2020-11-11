# Inserting a node at the end of a linked list
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
            print(print_val.data,end = " ")
            print_val = print_val.next_val

    def at_end(self,new_data):
        # assigning new_data of class node to new_Node
        new_node = Node(new_data)
        # check if linked list is empty if yes assign the new node as the head_val and return
        if self.head_val==None:
            self.head_val = new_node
            return
        # if it is an empty linked list then assign the head of the linked list to a variable
        x = self.head_val
        # check if the next value is none. if not none then assign the next value to x
        # if none assign the new_node to the next value.
        while x.next_val:
            x = x.next_val
        x.next_val = new_node
list = linked_list()
list.head_val = Node("first name")
e2 = Node("middle name")
e3 = Node("last name")
list.head_val.next_val = e2
e2.next_val = e3
list.at_end("sai sharan konety")
list.print_list()
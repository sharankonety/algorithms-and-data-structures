# Inserting a node in between two nodes in a linked list
class Node:
    def __init__(self,data=None,next_val=None):
        self.data = data
        self.next_val = next_val
class linked_list:
    def __init__(self,head_val=None):
        self.head_val = head_val
    def in_between(self,pre_node,new_data):
        new_node = Node(new_data)
        # to check if there is a pre node.
        if pre_node is None:
            print ("there is no pre node")
            return
        # if yes assign the next val of pre node as the next val of new node
        new_node.next_val = pre_node.next_val
        # and assign the new node as the next val of pre node
        pre_node.next_val = new_node
    def print_list(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data,end = " ")
            print_val = print_val.next_val
list = linked_list()
list.head_val = Node("Konety")
e2 = Node("Sharan")
list.head_val.next_val = e2
list.in_between(list.head_val,"Sai")
list.print_list()

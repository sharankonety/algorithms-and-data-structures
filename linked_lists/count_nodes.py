class Node:
    def __init__(self,data=None):
        self.data = data
        self.next_val = None
class Linked_list:
    def __init__(self,head=None):
        self.head = head
    def print_list(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next_val
    def count_list(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next_val
        print(count)
    def at_beginning(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        new_node.next_val = self.head
        self.head = new_node
    def at_end(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        x = self.head
        while x.next_val is not None:
            x = x.next_val
        x.next_val = new_node
    def in_between(self,pre_node,new_data):
        new_node = Node(new_data)
        if pre_node is None:
            print("there is no previous node")
        new_node.next_val = pre_node.next_val
        pre_node.next_val = new_node
list = Linked_list()
list.head = Node("Hey!")
e2 = Node("There ?")
list.head.next_val = e2
list.at_beginning("lala")
list.at_end("asdf")
list.in_between(list.head,"Hola")
list.print_list()
list.count_list()

# program to insert in a new node in a sorted linked list
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def display(self):
        print_val = self.head
        while print_val:
            print(print_val.data,end="-->")
            print_val = print_val.next
        print("/0")
    def add_data(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def insert_in_sort(self,key):
        new_node = Node(key)
        temp = self.head
        q = None
        if temp is None:
            self.head = new_node
        else:
            while temp and temp.data <= key:
                q = temp
                temp = temp.next
            if temp == self.head:
                self.head = new_node
                new_node.next = temp
            else:
                new_node.next = q.next
                q.next = new_node
list = Linked_list()
list.add_data(4)
list.add_data(6)
list.add_data(8)
list.add_data(9)
list.display()
# list.insert_in_sort(11)
list.insert_in_sort(1)
list.display()
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def count_list(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print(count)
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
list = Linked_list()
list.add_data(1)
list.add_data(2)
list.add_data(3)
list.add_data(4)
list.add_data(5)
list.display()
list.count_list()
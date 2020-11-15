# program to find the middle node in the linked list
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
            print(print_val.data,end = "-->")
            print_val = print_val.next
        print("/0")
    def middle_node(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        temp = self.head
        for i in range(count//2):
            temp = temp.next
        x = temp.data
        print("node: ",x)
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
# list.add_data(2)
# list.add_data(3)
list.display()
list.middle_node()
class Node:
    def __init__(self,data):
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
    def reverse(self):
        p = self.head
        q = None
        r = None
        while p:
            r = q 
            q = p 
            p = p.next
            q.next = r
        self.head = q
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
list.add_data(5)
list.add_data(8)
list.add_data(10)
list.display()
list.reverse()
list.display()


class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Circular_linked_list:
    def __init__(self):
        self.head = None
        self.last = None
    def insert(self,new_data):
        if self.head == None:
            new_node = Node(new_data)
            self.head = new_node
            self.last = new_node
            new_node.next = new_node
            return
        new_node = Node(new_data)
        new_node.next = self.head
        self.last.next = new_node
        self.last = new_node

def display(head):
    print_val = head
    print(print_val.data,end="-->")
    print_val = print_val.next
    while print_val != head:
        print(print_val.data,end="-->")
        print_val = print_val.next
a = Circular_linked_list()
a_nodes = [1,2,3,4,5]
for x in a_nodes:
    a.insert(x)
display(a.head)


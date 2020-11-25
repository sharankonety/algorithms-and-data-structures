# program to delete a node from the circular linked list.
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=next
class circular_linked_list:
    def __init__(self):
        self.head = None
        self.last = None
    def insert(self,new_data):
        if self.head is None:
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
    p = head
    print(p.data,end="-->")
    p = p.next
    while p!=head:
        print(p.data,end="-->")
        p= p.next
    print("")
a = circular_linked_list()
def delete_node(head,key):
    if head is None:
        return
    if head.data == key and head.next == head:
        head = None
    last = head
    q = None
    if head.data == key:
        while last.next != head:
            last = last.next
        last.next = head.next
        head = last.next
    while last.next != head and last.next.data != key:
        last = last.next
    if last.next.data == key:
        q = last.next
        last.next = q.next
    else:
        print("No such key")
a_nodes = [1,2,3,4,5]
for x in a_nodes:
    a.insert(x)
display(a.head)
delete_node(a.head,2)
display(a.head)


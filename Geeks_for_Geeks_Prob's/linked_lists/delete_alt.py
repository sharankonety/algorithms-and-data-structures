# program to delete alternate nodes in a linked list
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def insert(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp=self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
def delete_alt(head):
    if head is None:
        return
    p = head
    q = head.next
    while q:
        p.next = q.next
        q = None
        p = p.next
        if p:
            q = p.next
def display(head):
    while head:
        print(head.data,end="-->")
        head = head.next
    print("/0")
a = linked_list()
a_nodes = [1,2,3,4,5]
for x in a_nodes:
    a.insert(x)
display(a.head)
delete_alt(a.head)
display(a.head)
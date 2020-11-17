# program to merge two sorted linked lists
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list():
    def __init__(self):
        self.head = None
    def insert(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
def display(n):
    while n:
        print(n.data,end="-->")
        n = n.next
    print("/0")
def merge(head_a,head_b):
    if head_a.data < head_b.data:
        head_c = last = head_a
        head_a = head_a.next
        last.next = None
    else:
        head_c = last = head_b
        head_b = head_b.next
        last.next = None
    while head_a and head_b:
        if head_a.data < head_b.data:
            last.next = head_a
            last = head_a
            head_a = head_a.next
            last.next = None
        else:
            last.next = head_b
            last = head_b
            head_b = head_b.next
            last.next = None
    if head_a:
        last.next = head_a
    else:
        last.next = head_b
    return head_c
if __name__=="__main__":
    a = Linked_list()
    b = Linked_list()
    nodes_a = [5,10,15,40]
    nodes_b = [2,3,20]
    for x in nodes_a:
        a.insert(x)
    for x in nodes_b:
        b.insert(x)
    display(a.head)
    display(b.head)
    display(merge(a.head,b.head))
   

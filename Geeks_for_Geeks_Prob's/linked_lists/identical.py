# program to check if the two linked lists are identical or not.
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def insert(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
def is_identical(head1,head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    return True
def display(head):
    while head:
        print(head.data,end="-->")
        head = head.next
    print("/0")
a = Linked_list()
b = Linked_list()
a_nodes = [1,2,3,4]
b_nodes = [99,108,23]
for x in a_nodes:
    a.insert(x)
for x in b_nodes:
    b.insert(x)
display(a.head)
display(b.head)
if is_identical(a.head,b.head) is True:
    print("Identical")
else:
    print("Not Identical")
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def print_list(self):
        print_val = self.head
        while print_val:
            print(print_val.data,end="-->")
            print_val = print_val.next
        print("/0")
    # function to remove duplicates in a sorted linked list
    # we need two pointers to check if there are any duplicate elements one pointed to the head node and the other one to the next 
    # of head node
    def remove_dup(self):
        p = self.head
        q = p.next
        # when q is not none then if the data of p matches with data of q the assign q's next to p'next and delete q
        # then assign p's next to q.
        while q:
            if p.data == q.data:
                p.next = q.next
                del q
                q = p.next
            # if the data doesn't match then traverse through the linked list using p and q
            else:
                p = q
                q = q.next
list = Linked_list()
list.head = Node(3)
e2 = Node(5)
e3 = Node(5)
e4 = Node(8)
e5 = Node(8)
e6 = Node(8)
list.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
list.print_list()
list.remove_dup()
list.print_list()
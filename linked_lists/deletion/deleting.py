class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None
    def Print_list(self):
        print_val = self.head
        while print_val:
            print(print_val.data,end="-->")
            print_val = print_val.next
        print("/0")
    # Function to delete the node having the key value
    def delete_node(self,key):
        # here we need two pointers to point the previous node of the deleted node to the next node of the deleted node.
        # so we assign one pointer(p) to the head node and another pointer(q) to None so q is following the pointer. 
        p = self.head
        q = None
        # we have two cases 1.key in 1st node 2.key in any other node
        # 1. when p is not none and the key value matches with the head node then assign p's next as the head node and assign p as None
        if p and p.data == key:
            self.head = p.next
            p = None
            return
        # 2. when p is not none and while checking if the key matches with p's data keep traversing with p and q in the linked list
        # if the key matches with the data in p then assign p's next to q's next
        while p:
            if p.data == key:
                q.next = p.next
                p = None
            else:
                q = p
                p = p.next
list = Linked_list()
list.head = Node(1)
e2 = Node(2)
e3 = Node(3)
list.head.next = e2
e2.next = e3
list.Print_list()
list.delete_node(2)
list.Print_list()

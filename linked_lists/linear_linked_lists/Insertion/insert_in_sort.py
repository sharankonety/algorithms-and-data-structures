# Inserting a node in a sorted linked list
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
    # function to insert a node in a sorted linked list
    def insert_in_sort(self,key):
        # first assign a pointer to the head of linked list and one tail pointer assigned to none following it.
        p = self.head
        q = None
        new_node = Node(key)
        # here we have to check two cases 1.empty linked list 2. linked list with a key less than the head node 
        # 3. linked list with a key to be inserted at normal position(other than head).
        # first check if the head node is none, if yes assign new_node as the head node  
        if p is None:
            self.head = new_node 
        # if not while p is not None and the data of p less than or equal to key traverse in the loop with q and p
        else:
            while p and p.data<= key:
                q = p
                p = p.next
            # if the key value is less than the value of the head node, then assign the new_node as the head and p as next of newnode 
            if p == self.head:
                self.head = new_node
                new_node.next = p
            # else then key is at random position then assign next of q to next of new_node and new_node as the next of q
            else:
                new_node.next = q.next
                q.next = new_node
list = Linked_list()
list.head = Node(9)
e2 = Node(10)
e3 = Node(13)
list.head.next = e2
e2.next = e3
list.insert_in_sort(11)
list.Print_list()

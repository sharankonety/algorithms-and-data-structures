# search a key element in the linked list
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self,head=None):
        self.head=head
    def list_print(self):
        print_val=self.head
        while print_val != None:
            print(print_val.data)
            print_val = print_val.next
    def search_list(self,key):
        search_val = list.head
        while search_val != None:
            if key==search_val.data:
                print("found")
            search_val = search_val.next
list = linked_list()
list.head = Node(32)
e2 = Node(23)
e3 = Node(56)
list.head.next = e2
e2.next = e3
list.list_print()
list.search_list(56)

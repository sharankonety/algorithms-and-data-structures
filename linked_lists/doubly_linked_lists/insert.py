# insert at particular position using the previous node in a doubly linked list
class Node:
    def __init__(self,data=None):
        self.pre = None
        self.data = data
        self.next = None
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.pre = None
            self.tail.next = None
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
            self.tail.next = None
    def insert_at_head(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.pre = None
            self.tail.next = None
        else:
            self.head.pre = new_node
            new_node.next = self.head
            self.head = new_node
            self.head.pre = None
    def insert_after(self,pre_key,key):
        new_node = Node(key)
        temp = self.head
        while temp:
            if temp.data == pre_key:
                new_node.next = temp.next
                new_node.pre = temp
                if temp.next:
                    temp.next.pre = new_node
                temp.next = new_node
                return
            else:
                temp = temp.next
def display(head):
    x = head
    while x:
        print(x.data,end="-->")
        x = x.next
a = doubly_linked_list()
a_nodes = [1,2,3,4,5]
for x in a_nodes:
    a.insert(x)
a.insert_at_head(0)
a.insert_after(5,6)
display(a.head)
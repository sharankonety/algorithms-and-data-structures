# program to delete multiple occurences of keys
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class linked_list:
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
    def delete(self,x):
        temp = self.head
        q = None
        if self.head and self.head.data == x:
            self.head = temp.next
            temp = self.head
        while temp:
            while temp and temp.data != x:
                q = temp
                temp = temp.next
            if temp == None:
                return self.head
            else:
                q.next = temp.next
                temp = q.next 
def display(n):
    while n:
        print(n.data,end="-->")
        n = n.next
    print("/0")
a = linked_list()
a_nodes = [2,2,1,4,4]
for x in a_nodes:
    a.insert(x)
display(a.head)
a.delete(4)
display(a.head)
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
def concatenate(head_a,head_b):
    temp = last = head_a
    while last.next:
        last = last.next
    last.next = head_b
    return temp
if __name__=="__main__":
    a = Linked_list()
    b = Linked_list()
    a_nodes = [1,2,3,4]
    b_nodes = [5,6,7,8]
    for x in a_nodes:
        a.insert(x)
    for x in b_nodes:
        b.insert(x)
    # display(a.head)
    # display(b.head)
    display(concatenate(a.head,b.head))

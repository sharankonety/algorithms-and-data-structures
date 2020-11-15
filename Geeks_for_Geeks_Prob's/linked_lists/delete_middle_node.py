# progrom to delete the middle node
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
        print("/0")
    def add_data(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def del_middle(self):
        count = 0
        temp = self.head
        prev = None
        while temp:
            count += 1
            temp = temp.next
        temp = self.head
        for i in range(count//2):
            prev = temp
            temp = temp.next
        print(temp.data)
        prev.next = temp.next
list = Linked_list()
list.add_data(1)
list.add_data(3)
list.add_data(5)
list.add_data(7)
list.add_data(9)
list.display()
list.del_middle()
list.display()
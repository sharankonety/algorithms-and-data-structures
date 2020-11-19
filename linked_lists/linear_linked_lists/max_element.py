# maximum element in a linked list
class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None
class Linked_list:
  def __init__(self,head=None):
    self.head = head
  def list_print(self):
    print_val = self.head
    while print_val is not None:
      print(print_val.data)
      print_val = print_val.next
  def list_max(self):
    max = 0
    temp = self.head
    while temp is not None:
      if max < temp.data:
        max = temp.data
      temp = temp.next
    print("max element: ",max)
list = Linked_list()
list.head = Node(1)
e2 = Node(5)
e3 = Node(3)
list.head.next = e2
e2.next = e3
list.list_print()
list.list_max()
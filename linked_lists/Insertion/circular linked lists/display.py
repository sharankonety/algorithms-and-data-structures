class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None
class c_linked_list:
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
    new_node.next = self.head
def display(n):
    temp = n
    if temp:
        print(temp.data,end="-->")
        while temp.next != n:
            print(temp.data)
a = c_linked_list()
a_nodes = [1,2,3,4,5]
for x in a_nodes:
  a.insert(x)
display(a.head)
# program to traverse the tree in level order.
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def Insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.Insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.Insert(data)
        else:
            self.data = Node(data)
def Level_order(Queue):
    if len(Queue)==0:
        return
    N = Queue[0]
    Queue.pop(0)
    if N.left:
        Queue.append(N.left)
    if N.right:
        Queue.append(N.right)
    print(N.data,end = " ")
    Level_order(Queue)
root = Node(9)
Queue = []
Queue.append(root)
root.Insert(5)
root.Insert(11)
root.Insert(3)
root.Insert(6)
root.Insert(10)
root.Insert(14)
Level_order(Queue)
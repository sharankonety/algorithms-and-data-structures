# Program to count the total number of nodes in a Binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = Node(data)
def count_nodes(Node):
    if Node is None:
        return 0
    return 1 + count_nodes(Node.left) + count_nodes(Node.right)
root = Node(9)
root.insert(5)
root.insert(11)
root.insert(3)
root.insert(6)
root.insert(10)
root.insert(14)
print(count_nodes(root))
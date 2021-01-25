# program to find the height of the binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def height(Node):
    if Node is None:
        return -1
    return max(height(Node.left),height(Node.right))+1
root = Node(9)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(5)
root.left.right.left = Node(2)
print(height(root))
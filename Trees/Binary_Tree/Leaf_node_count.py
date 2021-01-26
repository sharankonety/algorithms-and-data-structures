# Program to find the total number of leaf nodes in a binary tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def Leaf_node_count(Node):
    if Node:
        if Node.left is None and Node.right is None:
            return Leaf_node_count(Node.left)+Leaf_node_count(Node.right)+1
        else:
            return Leaf_node_count(Node.left)+Leaf_node_count(Node.right)
    return 0

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(Leaf_node_count(root))
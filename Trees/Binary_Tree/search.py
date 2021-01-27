# program to search if a node exists in a tree or not.
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
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data,end=" ")
        if self.right:
            self.right.PrintTree()
def search(Node,key):
    if Node is None:
        return 
    if Node.data == key:
        return True
    elif key>Node.data:
        return search(Node.right,key)
    elif key<Node.data:
        return search(Node.left,key)
root = Node(25)
root.insert(20)
root.insert(30)
root.insert(19)
root.insert(21)
root.insert(29)
root.insert(31)
root.PrintTree()
print("")
print(search(root,29))
# program to implement a stack using array
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def display(self):
        print(self.stack)
a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.display()
print(a.top())
a.pop()
a.display()
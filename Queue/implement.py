# Program to implement a Queue
class Queue:
    def __init__(self):
        self.queue = []
    def push(self,data):
        self.queue.append(data)
    def pop(self):
        self.queue.pop(0)
    def display(self):
        print(self.queue)
a = Queue()
b = [1,2,3,4,5]
for x in b:
    a.push(x)
a.display()
a.pop()
a.display()
a.pop()
a.display()

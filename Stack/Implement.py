# Program to implement a stack
stack = []
n = 5
def push(item):
    if len(stack) >= n:
        print("stack overflow")
        return
    else:
        stack.append(item)
def pop():
    if len(stack)<=0:
        print("Stack underflow")
    else:
        stack.pop()
a = [1,2,3,4,5,6,7]
for x in a:
    push(x)
print(stack)
pop()
print(stack)


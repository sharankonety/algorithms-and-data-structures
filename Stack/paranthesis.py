# program to check if the paranthesis in the given expression are balanced or not.
def is_balanced(exp):
    stack = []
    for i in exp:
        if i=='(':
            stack.append(i)
        elif i==')':
            stack.pop()
    if stack:
        return False
    else:
        return True
Exp = '((a+b)*(c-d))'
if is_balanced(Exp):
    print("Balanced")
else:
    print("Not balanced")



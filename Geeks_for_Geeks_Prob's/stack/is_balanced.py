# program to check if the pairs and the order of the brackets is correct.
def is_balanced(exp):
    stack = []
    for i in exp:
        if i=='{' or i=='[' or i=='(':
            stack.append(i)
        elif i=='}':
            if stack and stack[-1]=='{':
                stack.pop()
            else:
                return False
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                return False
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True
Exp = "[()]{}{[()()]()}"
if is_balanced(Exp):
    print("Balanced")
else:
    print("Not Balanced")

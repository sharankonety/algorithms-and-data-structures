# program to convert an infix expression to a postfix expression
operators = set(['+','-','*','/','(',')','^'])
priority = {'+':1,'-':1,'*':2,'/':2}
def conversion(exp):
    output = ''
    stack = []
    for ch in exp:
        if ch not in operators:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[ch]<=priority[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    if stack:
        output += stack.pop()
    return output
exp = '(A+(C+D*F+T*A)*B/C)'
print('Infix expression = ',exp)
print('postfix expression = ',conversion(exp))
# program to evaluate a postfix expression
operators = {'+','-','/','*','%','**'}
def evaluate(exp):
    stack = []
    for _ in exp:
        if _ not in operators:
            stack.append(_)
        else:
            a = stack.pop()
            b = stack.pop()
            if _ == '+':
                result = int(b)+int(a)
            elif _ == '-':
                result = int(b)-int(a)
            elif _ == '/':
                result = int(b)/int(a)
            elif _ == '*':
                result = int(b)*int(a)
            elif _ == '%':
                result = int(b)%int(a)
            elif _ == '**':
                result = int(b)**int(a)
            stack.append(result)
    return stack    
exp = '35*62/+4-'
print('postfix expression: ',exp)
print('result: ',evaluate(exp))

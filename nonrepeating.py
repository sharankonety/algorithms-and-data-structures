# test_case1: 'hello'  op = 'h'
# test_case2: 'zxvczbtxyzvy' op = 'c'
# test_case3: 'xxyyzz' op = -1
# print the first non repeating character in a string. if no such character print -1.
string = 'zxvczbtxyzvy'
output = -1
for char in string:
    if string.count(char)==1:
        output = char
        break
print(output)



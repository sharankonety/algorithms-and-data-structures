# print the first letters of each word in the string.
str = 'Geeks for geeks'
n = len(str)
result = str[0]
for i in range(n):
    if str[i]==' ':
        result += str[i+1]
print(result)

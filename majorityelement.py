# if an element occurs more than n/2 times print the element else print -1
list = [3,1,3,3,2]
n = len(list)
num = -1
for i in list:
    count = 0
    for j in list:
        if (i == j):
            count += 1
    if(count > n//2):
        num = i
print(num)

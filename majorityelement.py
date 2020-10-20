# if an element occurs more than n/2 times print the element else print -1
list = [3,1,3,3,2]
n = len(list)
num = -1
for i in list:
    print("i: ",i)
    count = 0
    for j in list:
        print("j: ",j)
        if (i == j):
            count += 1
            print("count: ",count)
    if(count > n//2):
        num = i
print(num)
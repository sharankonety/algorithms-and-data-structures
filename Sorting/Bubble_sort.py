# Bubble sort
# a = [3,1,9,8,5]
a = [1,3,5,8,9]
n = len(a)
for i in range (n-1):
    flag = 0
    for j in range (n-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            flag = 1
    if flag == 0:
        break
print(a)

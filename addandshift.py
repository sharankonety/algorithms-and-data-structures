list = [2,4,5,0,0,5,5,4,8,6,0,6,8]
list1 = []
list2 = []
n = len(list)
current = 0
next = 1
for i in range(n-1):
    if (list[i+1]!= 0):
        if (list[current] == list[next]):
            list[current] = 0
            list[next] *= 2
            current = i + 1
            next = i + 2
        else:
            current += 1
            next += 1
    else:
        next += 1
for j in range(n):
    if (list[j]!=0):
        list1.append(list[j])
    else:
        list2.append(list[j])
print(list1 + list2)

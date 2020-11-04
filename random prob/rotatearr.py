list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
n = len(list1)
d = 3
list2 = []

for i in range (d-1,-1,-1):
    list2.append(list1[i])
for i in range (n-1,d-1,-1):
    list2.append(list1[i])
l = len(list2)
for i in range(l-1,-1,-1):
    print(list2[i],end = " ")


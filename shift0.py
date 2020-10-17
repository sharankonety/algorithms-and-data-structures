list_1 = [2,3,4,0,0,5,5,4,8,6,0,6,8]
n = len(list_1)
list_2 = []
for i in range(n-1):
    if (list_1[i]==list_1[i+1]):
        list_1[i+1] += list_1[i]
        list_1[i] = 0
    if(list_1[i]==0):
        list_1.pop(i)
        list_2.append(0)
list_3 = list_1 + list_2
print(list_3)
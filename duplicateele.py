list = [3,6,8,8,10,12,15,15,15,20]
n = len(list)
dup = 0
for i in range(n-1):
    if(list[i] == list[i+1] & list[i] != dup):
        print(list[i])
        dup = list[i]

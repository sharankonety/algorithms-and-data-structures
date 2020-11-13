list = [19,2,31,45,6,11,121,27]
n = len(list)
for i in range(n-1,0,-1):
    print("iteration i: ",i)
    for j in range(i):
        print("iteration j: ",j)
        print("list[j]: ",list[j])
        print("list[j+1]: ",list[j+1])
        if list[j]>list[j+1]:

            temp = list[j]
            print("temp: ",temp)
            list[j] = list[j+1]
            list[j+1] = temp
            print(list)
print(list)

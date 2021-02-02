# Program to perform selection sort
arr = [3,1,9,8,5]
n = len(arr)
for i in range(n-1):
    k = i
    for j in range(i+1,n):
        if arr[j]<arr[k]:
            k = j
    arr[k],arr[i]=arr[i],arr[k]
print(arr)
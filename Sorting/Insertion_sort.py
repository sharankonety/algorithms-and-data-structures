# Program to perfrom Insertion sort
arr = [3,1,9,8,5]
n = len(arr)
for i in range(1,n):
    j = i-1
    x = arr[i]
    while j>-1 and arr[j]>x:
        arr[j+1]=arr[j]
        j -= 1
    arr[j+1]=x
print(arr)

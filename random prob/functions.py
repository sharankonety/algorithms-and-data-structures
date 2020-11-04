def get(x):
    if (x>=0 & x<n) :
        return list[x]

def max(arr):
    maximum = arr[0]
    for i in range(1,n):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum



list = [1,2,3,4,5]
n = len(list)
result = max(list)
print (result)
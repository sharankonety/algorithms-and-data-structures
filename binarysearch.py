def binsrc(arr, low, high, key):
    while(low<=high):
        mid = (low+high)//2
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
    return -1
array = [1, 2, 3, 8, 23, 5]
array.sort()
l = 0
h = len(array) - 1
k = 25
result = binsrc(array, l, h, k)
if result == -1:
    print("element not in array")
else:
    print (result)
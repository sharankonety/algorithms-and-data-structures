# testcase 1 : 7 10 4 3 20 15 k=3 print the third smallest element output = 7
# testcase 2 : 7 10 4 20 15 k = 4 output = 200
# where all the elements in the list are distinct
list = [7,10,4,20,15]
k = 4
list.sort()
print(list[k-1])

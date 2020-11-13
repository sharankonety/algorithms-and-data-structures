import numpy as np
r = int(input("enter no. of rows: "))
c = int(input("enter no. of columns: "))
entries = list(map(int,input().split()))
matrix = np.array(entries).reshape(r,c) 
print(matrix)



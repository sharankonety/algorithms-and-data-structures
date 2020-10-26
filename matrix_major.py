import numpy as np
def lower_triangle(matrix, row, column):
  for i in range(0,row):
    for j in range(0,column):
      if (i<j):
        print("0", end = " ")
      else:
        print(matrix[i][j], end = " ")
    print(" ")
def upper_triangle(matrix, row, column):
  for i in range(0,row):
    for j in range(0,column):
      if(i>j):
        print("0", end=" ")
      else:
        print(matrix[i][j], end= " ")
    print(" ")
list = np.array([1,2,3,4,5,6,7,8,9])
row = 3
column = 3
matrix = list.reshape(row,column)
lower_triangle(matrix, row, column)
print("")
upper_triangle(matrix,row,column)
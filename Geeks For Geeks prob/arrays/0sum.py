# Largest Subarray with 0 sum
# given a list of positive and negative integers, print the largest subarray whose sum is 0.
list = [15,-2,2,-8,1,7,10,23]
n = len(list)
length = 0
for i in range(n):
  # print("i: ",i)
  sum = 0
  for j in range(i,n):
    # print("j: ",j)
    # print("list[j]: ",list[j])
    sum += list[j]
    # print("sum: ",sum)
    if sum == 0 and length <j-i+1:
      length = j-i+1
      print("length: ",length)
print(length)
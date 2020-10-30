# peak element
# From the given list print the index of the peak element
# If the element in the list is greater than it's neighbours then it is a peak element
list = [1,2,3]
n = len(list)
if list[0]>list[1]:
  print(0)
if list[n-1]>list[n-2]:
  print(n-1)
for i in range(1,n-1):
  if ((list[i]>list[i-1]) and (list[i]>list[i+1])):
    print(i)
  
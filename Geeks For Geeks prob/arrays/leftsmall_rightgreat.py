# input list [4,2,5,7] 
# from the given list print the first number which has lesser number on the left side
# and a higher number on the right side. if no such element in the list print -1.
list = [4,2,5,7]
n = len(list)
no_element = -1
for i in range(1,n-1):
  if(list[i-1]<list[i] and list[i]<list[i+1]):
    no_element = list[i]
    break
print(no_element)
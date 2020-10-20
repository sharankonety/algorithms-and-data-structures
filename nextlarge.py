# input: [1,3,2,4]
#output: check if there is next larger element if yes print it, if no such element print -1.

list = [9]
n = len(list) 
for i in range(n):
  next_large = -1
  print("i iteration: ",i)
  for j in range(i+1,n):
    print("j iteration: ",j)
    print("element i: ",list[i])
    print("element j: ",list[j])
    if (list[j]>list[i]):
      next_large = list[j]
      break
  print(next_large)
  
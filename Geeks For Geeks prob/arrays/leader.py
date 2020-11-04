list = [16,17,4,3,5,2]
n = len(list)
for i in range(n):
  is_leader = True
  for j in range(i+1,n):
    if (list[j] > list[i]):
      is_leader = False
      break
  if is_leader == True :
    print(list[i]) 
      
      
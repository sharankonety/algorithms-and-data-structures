'''[10,20,20,10,10,30,50,10,20] The elements in the list indicate the color of the socks and the final output is to 
print the no. of pairs present in the list and if no pair exists print 0''' 
# test case1 : 10 20 20 10 10 30 50 10 20   number of pairs = 3 [10,10] and [20,20] and [10,10] leftover socks = 30,50,20
# test case2 : 1 2 1 2 1 3 2   number of pairs = 2 [1,1] [2,2] leftover socks = 1,3,2
# test case3 : 1 2 3 4 5 number of pairs = 0
list = [1,2,3,4,5]
n = len(list)
pair_count = 0
for i in range(n):
  print(" i iteration: ",i)
  for j in range(i+1,n):
    print("j iteration: ",j)
    print("list[i]: ",list[i])
    print("list[j]: ",list[j])
    if list[i]==list[j] and list[i]!=0:
      pair_count += 1
      list[i] = list[j] = 0
      break
print("pair_count: ",pair_count)  


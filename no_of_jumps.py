# input: a list [1,3,5,8,9,2,6,7,8,9]
# output : print the number of jumps required to reach the end of the list. if impossible return -1.
list = [1,3,5,8,9,2,6,7,8,9]
n = len(list)
jump_count = 0
i = 0
while(i < n-1):
  jump = list[i]
  print("jump: ",jump)
  if(jump == 0):
    jump_count = -1
    break
  else:
    i += jump
    print("i: ",i)
    jump_count += 1
    print("jump count: ",jump_count)
print("final output: ",jump_count)

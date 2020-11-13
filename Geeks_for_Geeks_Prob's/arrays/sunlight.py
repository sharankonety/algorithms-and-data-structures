# the given list contains the height of the bulidings.the buildings recieve sunlight starting from the left.
# If there is any building of certain height,all the buildings to the right with lesser height cannot recieve the sunlight.
# print the no. of buildings that receive sunlight
# input: 6 2 8 4 11 13, buildings which recieve sunlight = 6,8,11,13, ,output: 4
list = [6,2,8,4,11,13]
n = len(list)
count = 1
start = list[0]
for i in range(1,n):
  if list[i]>start:
    print(list[i])
    start = list[i]
    count += 1
print(count)

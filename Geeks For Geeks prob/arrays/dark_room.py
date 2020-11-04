# The list indicates the size of candles in a room and the size of candle decreases by 1 unit every day.
# print the maximum number of days the room is without darkness.
# list = [1,1,2], day 1 list = [0,0,1],day2 list= [0,0,0] so the maximum no. of days is 2
# list = [2,3,4,2,1], 1:[1,2,3,1,0],2:[0,1,2,0,0],3:[0,0,1,0,0] 4:[0,0,0,0,0] output = 4
list = [374176, 393338, 397305, 230094, 78526 ,16313, 402977, 253905, 365773, 660052, 501595, 78077, 40290, 989183, 791126, 151262, 927383, 712114, 75279, 854177, 630261, 374991, 288133, 406306, 439849, 722240, 770431, 432780, 806733,201099]
n = len(list)
max = list[0]
for i in range(n):
    if list[i]>max:
        max = list[i]
print(max)

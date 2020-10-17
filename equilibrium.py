list = [1,3,5,2,2]
n = len(list)
for i in range(1,n-1):
    left_sum = 0
    right_sum = 0
    for j in range(i):
        left_sum += list[j]
    for j in range(i+1,n):
        right_sum += list[j]
    if left_sum==right_sum:
        print(i)
    
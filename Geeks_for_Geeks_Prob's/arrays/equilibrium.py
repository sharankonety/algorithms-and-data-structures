list = [1,3,5,2,2]
n = len(list)
for i in range(1,n-1):
    # print("iteration i: ",i)
    left_sum = 0
    # print("left_sum: ",left_sum)
    right_sum = 0
    # print("right_sum: ",right_sum)
    for j in range(i):
        # print("iteration j1: ",j)
        left_sum += list[j]
        # print("left_sum: ",left_sum)
    for j in range(i+1,n):
        # print("iteration  j2: ",j)
        right_sum += list[j]
        # print("right_sum: ",right_sum)
    if left_sum==right_sum:
        print(i)

    
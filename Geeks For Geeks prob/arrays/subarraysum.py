# sub array sum
# print the index values of the start and end indices of the array which lead to the given sum
list = [1,2,3,7,5]
n = len(list)
actual_sum = 12
for i in range(n):
    current_sum = list[i]
    for j in range(i+1,n):
        current_sum += list[j]
        if current_sum==actual_sum:
            print(i,j)
        if current_sum > actual_sum:
            break

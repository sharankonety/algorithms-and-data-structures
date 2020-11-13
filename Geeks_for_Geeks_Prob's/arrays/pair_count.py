# Print the total number of pairs whose sum equals the given key.
# list = [1,5,7,1] ,key = 6 then (1,5) and (5,1) so Pair_count = 2
list = [1,1,1,1]
n = len(list)
key = 2
pair_count = 0
for i in range(n):
  for j in range(i+1,n):
    if list[i]+list[j] == key:
      pair_count += 1
print(pair_count)
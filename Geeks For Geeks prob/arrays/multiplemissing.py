list=[5,6,7,9,11]
n = len(list)
diff = 5
for i in range(0,n):
  if (list[i]-i != diff):
    while(diff<list[i]-i):
      print(i+diff)
      diff += 1

      
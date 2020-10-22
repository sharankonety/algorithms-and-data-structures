# print the duplicates in the string.
string = 'geeksforgeeks'
duplicate = []
for char in string:
  if(string.count(char)>1):
    if char not in duplicate:
      duplicate.append(char)
print(duplicate)
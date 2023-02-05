s = input() 
index = [0] * 26 #97~122
for i in s:
   index[ord(i)-97] = s.count(i)
for i in index:
    print(i, end=" ")
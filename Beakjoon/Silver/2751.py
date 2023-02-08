import sys
n= int(sys.stdin.readline().strip())
a = []
for i in range(n):
    b = int(sys.stdin.readline().strip())
    a.append(b)
a.sort()
for i in a:
    print(i)
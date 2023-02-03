x = list(map(int,input().split()))
n = []
for i in x:
    n.append(i*i)
print(sum(n) % 10)
t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    pp = [i for i in range(1,n+1)]
    for x in range(k):
        for y in range(1,n):
            pp[y] += pp[y-1]
    print(pp[-1])
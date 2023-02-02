a = []
b = []
for i in range(10000):
    b.append(i)
    res = i + sum(map(int,str(i)))
    a.append(res)
c = list(set(b)-set(a))
c.sort()
for i in c:
    print(i)
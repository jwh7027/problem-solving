n = []
for i in range(1,29):
    n.append(int(input()))
n.sort()
for i in range(1,31):
    if i not in n:
        print(i)
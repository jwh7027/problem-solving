x = input().upper()
max = 0
for i in set(x):
    n = x.count(i)
    if n > max:
        max = n
        cnt = i
    elif n == max:
        max = n
        cnt = '?'
    else:
        continue
print(cnt)

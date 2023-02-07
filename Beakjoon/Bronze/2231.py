n = int(input())
for i in range(1,n+1):
    a = sum([int(x) for x in str(i)])
    if n == i + a:
        result = i
        break
    else:
        result = 0
print(result)
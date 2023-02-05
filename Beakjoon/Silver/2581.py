m = int(input())
n = int(input())
a = []
for i in range(m,n+1):
    if i == 1: # 1 제외
        continue
    for j in range(2,i//2+1): # 검색 축소
        if i % j == 0:
            break
    else:
        a.append(i)

if a == [] :
    print(-1)
else:
    print(sum(a))
    print(min(a))
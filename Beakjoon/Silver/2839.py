n = int(input())
res = 0
while n >= 3:
    # 3의이면서 5의 배수가 아닌 경우 3키로 봉지에 담음
    if n % 3 == 0 and n % 5 !=0:
        res += 1
        n -=3
    else:
        # 나머지 경우 5키로 봉지에 담음
        res +=1
        n -= 5
if n != 0:
    print(-1)
else:
    print(res)

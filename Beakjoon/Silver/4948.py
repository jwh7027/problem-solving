import math
# 에라토스테네스의 체 이용
# 1. 2 * n 이하의 소수를 전부 구한다
# 2.n 부터 갯수를 구한다
N = 123456*2 + 1
prime = [True] * N
for i in range(2,int(math.sqrt(N))+1): # N의 최대 약수가 제곱근 n 이하이므로 제곱근 n까지 검사
    if prime[i]: # i가 소수인 경우
        for j in range(2*i,N,i): # i이후 i의 배수들을 False 판정
            prime[j] = False

while True:
    n = int(input())
    cnt = 0
    if n == 0: break
    else:
        for i in range(n+1,2*n+1):
            if prime[i]: cnt+= 1 # 소수 개수 세기
    print(cnt)
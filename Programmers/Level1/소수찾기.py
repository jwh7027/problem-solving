import math
def solution(n):
    answer = 0
    N = 1000000 * 2 + 1
    prime = [True] * N
    for i in range(2,int(math.sqrt(N))+1):
        if prime[i]:
            for j in range(2 * i,N,i):
                prime[j] = False

    for i in range(2,n+1):
        if prime[i]: answer +=1

    return answer
#더 간결한 에라토스테너스의 체
def solution(n):
    num=set(range(2,n+1))
    for i in range(2,int(math.sqrt(n))+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
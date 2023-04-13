def solution(n):
    fibo = [1,2]
    for i in range(2,n+1):
        fibo.append((fibo[i-1] + fibo[i-2]))
    return fibo[n-1] % 1234567
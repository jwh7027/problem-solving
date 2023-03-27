def solution(n):
    fibo = [0,1]
    for i in range(2,n+1):
        fibo.append((fibo[i-1] + fibo[i-2]) % 1234567)
    return fibo[-1]

def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a
def solution(n):
    m = n + 1
    a = ""
    b = ""
    while True:
        a = bin(n)[2:]
        b = bin(m)[2:]
        if a.count("1") == b.count("1") and n < m:
            break
        m += 1
    return m

#다른 풀이
def solution(n):
    num1 = bin(n).count("1")
    while True:
        n = n+1
        if num1 == bin(n).count("1"):
            break
    return n
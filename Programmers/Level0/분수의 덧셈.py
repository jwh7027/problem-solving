def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    
    a = numer
    b = denom
    #유클리드 호제법
    while b > 0:
        a,b = b , a % b
    #gcd 최대공약수
    gcd = a
    return numer / gcd ,denom / gcd
#유클리드 호제법
# A를 B로 나눈 몫을 Q라 하고, 나머지를 R이라할때, gcd(A,B) = gcd(B,R)
t = int(input())
for i in range(3):
    a,b = map(int,input().split())
    c,d = a,b
    while b>0:
        a,b = b, a % b
    print(int(c*d /a))

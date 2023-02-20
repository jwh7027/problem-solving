import math
def solution(balls, share):
    return math.factorial(balls) / (math.factorial(balls-share) * math.factorial(share))

# math함수 comb 조합 함수를 사용
def solution(balls, share):
    return math.comb(balls, share)

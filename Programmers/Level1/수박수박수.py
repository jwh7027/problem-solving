def solution(n):
    answer = '수'
    while n-1>0:
        if answer[-1] != "수":
            answer += "수"
            n -= 1
        else:
            answer += "박"
            n -= 1
    return answer

# 슬라이싱 풀이
def solution(n):
    str = "수박" * (n//2 + 1)
    return str[:n]
def solution(k, m, score):
    score = sorted(score,reverse =True)
    answer = []
    result = 0
    for i in range(0,len(score),m):
        answer.append(score[i:m+i])
    for apple in answer:
        if apple == m:
            result += min(apple) * m

    return result
#다른 풀이
def solution(k, m, score):
    score = sorted(score,reverse =True)
    result = 0
    for i in range(m-1,len(score),m):
        result += score[i] * m
    return result

#다른 풀이
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m
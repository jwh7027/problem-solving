def solution(k, m, score):
    score = sorted(score,reverse =True)
    answer = []
    result = 0
    for i in range(0,len(score),m):
        answer.append(score[i:m+i])
    for i in range(len(answer)):
        if len(answer[i]) == m:
            result += min(answer[i]) * m

    return result
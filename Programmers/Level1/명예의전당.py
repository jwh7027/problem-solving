def solution(k, score):
    answer = []
    score_ls = []
    for i in range(1,len(score)+1):
        score_ls.append(score[i-1])
        score_ls.sort(reverse=True)
        answer.append((i,score_ls[:k]))

    return [answer[i][1][-1] for i in range(len(answer))]

#다른풀이
def solution(k, score):
    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer

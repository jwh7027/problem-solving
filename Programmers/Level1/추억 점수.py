def solution(name, yearning, photo):
    answer = []
    score_ls = {}
    for a,b in zip(name,yearning):
        score_ls[a] = b

    for i in photo:
        temp = 0
        for j in i:
            temp += score_ls.get(j,0)
        answer.append(temp)
    return answer

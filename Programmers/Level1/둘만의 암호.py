def solution(s, skip, index):
    answer = ''
    ls = "abcdefghijklmnopqrstuvwxyz"
    alpha = []
    for i in skip:
        if i in ls:
            ls = ls.replace(i,"")

    for j in ls:
        alpha.append(j)

    for k in s:
        answer += alpha[(alpha.index(k) + index) % len(alpha)]
    return answer
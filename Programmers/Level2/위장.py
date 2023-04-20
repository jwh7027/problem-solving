def solution(clothes):
    answer = 1
    dic = {k : [] for _,k in clothes}
    for v,k in clothes:
        dic[k].append(v)

    for i in dic.values():
        answer *= (len(i) + 1)

    return answer - 1
def solution(s):
    answer = []
    s = s[2:-2].split("},{")

    s.sort(key = lambda x : len(x))
    #s.sort(key = len) # 가능
    for i in s:
        a = i.split(",")
        for j in a:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
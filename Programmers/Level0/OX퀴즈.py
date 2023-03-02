def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        p, a = quiz[i].split("=")
        if eval(p) == int(a):
            answer.append("O")
        else:
            answer.append("X")
    return answer
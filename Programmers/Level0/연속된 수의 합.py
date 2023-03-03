def solution(num, total):
    answer = []
    cnt = -100
    while True:
        for i in range(num):
            answer.append((cnt+i))
        if sum(answer) == total:
            return answer
        else:
            cnt += 1
            answer = []

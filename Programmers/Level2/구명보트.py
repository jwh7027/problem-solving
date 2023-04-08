from collections import deque
def solution(people, limit):
    answer = 0
    dq = deque(sorted(people))

    while dq:
        if len(dq) == 1:
            answer += 1
            break
        if dq[0] + dq[-1] <= limit:
            dq.popleft()
            dq.pop()
        else:
            dq.pop()
        answer += 1

    return answer
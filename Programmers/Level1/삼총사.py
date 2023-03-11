def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i):
            for k in range(j):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1   
    return answer

#combinations 조합 라이브러리 사용
from itertools import combinations
def solution(number):
    answer = 0
    l = list(combinations(number,3))
    for i in l:
        if sum(i) == 0:
            answer += 1
    return answer
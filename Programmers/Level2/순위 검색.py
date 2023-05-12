from collections import defaultdict
from itertools import combinations
from bisect import bisect_left as left_bound

def solution(info, query):
    answer = []
    people = defaultdict(list)
    
    #지원자의 데이터 경우의수 딕셔너리에 기록
    for i in info:
        person = i.split()
        score = int(person.pop())
        people[''.join(person)].append(score)
        
        for j in range(4):
            candi = list(combinations(person,j))
            for c in candi:
                people[''.join(c)].append(score)
                
    #기록한 딕셔너리의 성적 데이터를 모두 정렬
    for i in people: people[i].sort()
    
    #문의 조건에 따라 검색하고,나온 결과의 성적 배열을 이진탐색 하여 몇 명인지 확인
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-','')
        answer.append(len(people[key]) - left_bound(people[key], score))
    return answer
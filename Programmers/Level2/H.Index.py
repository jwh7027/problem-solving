def solution(citations):
    answer = 0
    citations = sorted(citations, reverse = True)
    for i in range(max(citations)):
        if len([j for j in citations if j>=i]) > answer:
            answer = i
    return answer
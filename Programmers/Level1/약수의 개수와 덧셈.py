def solution(left, right):
    answer = []
    for i in range(left,right+1):
        cnt = 0
        for j in range(1,i+1):
            if i % j == 0:
                cnt += 1
        if cnt & 1:
            answer.append(-i)
        else:
            answer.append(i)
    return sum(answer)  #시간복잡도 O(n**2)

def solution(left, right): #시간복잡도 O(n)
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer
def solution(number, limit, power):
    answer = []
    for i in range(1,number+1):
        cnt = 0
        for j in range(1,int(i**0.5)+1):
            if i == j ** 2:
                cnt += 1
            elif (i%j == 0):
                cnt += 2
        answer.append(cnt)
    res = [i if i <=limit else power for i in answer]
    return sum(res)
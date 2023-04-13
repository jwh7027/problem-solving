def solution(k, tangerine):
    answer = 0
    check = 0
    tangerine.sort()
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    arr = sorted(dic.items(), key = lambda x : x[1], reverse = True) #value 값을 기준으로 역순 정렬
    if arr[0][1] >= k:
        return 1
    else:
        for i in arr:
            if check < k:
                check += i[1]
                answer += 1
            else:
                break
    return answer
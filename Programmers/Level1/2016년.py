def solution(a, b):
    weeks = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = ''
    cnt = 0
    if a == 1:
        cnt = b % 7
        answer = weeks[cnt-1]
    else:
        for i in range(a-1):
            cnt += days[i]
        cnt +=b
        cnt %= 7
        answer = weeks[cnt-1]

    return answer
def solution(survey, choices):
    answer = ''
    dt = {'R' : 0, 'T' : 0, 'C' : 0, 'F' :0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    mapping = {1:3, 2:2, 3:1, 4: 0, 5:1,6:2,7:3}
    jipyo = [['R','T'], ['C','F'],['J','M'],['A','N']]

    #선택지 선택
    for i in range(0,len(choices)):
        choice = choices[i]
        if choice < 4:
            key = survey[i][0]
            dt[key] += mapping[choice]
        elif choice > 4:
            key = survey[i][1]
            dt[key] += mapping[choice]

    #결과 출력
    for j in jipyo:
        c1 = j[0]
        c2 = j[1]

        if dt[c1] == dt[c2]:
            if c1 < c2:
                answer += c1
            else:
                answer += c2
        elif dt[c1] > dt[c2]:
            answer +=c1
        else:
            answer +=c2
    return answer
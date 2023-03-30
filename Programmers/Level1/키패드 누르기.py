def solution(numbers, hand):
    answer = ''
    num2pos = {1 : (0,0),2 : (0,1),3 : (0,2),
           4 : (1,0),5 : (1,1),6 : (1,2,),
           7 : (2,0),8 : (2,1),9 : (2,2),
           0 : (3,1)}
    lh,rh = (3,0), (3,2)
    for number in numbers:
        np = num2pos[number]
        if number in [1,4,7]:
            answer +="L"
            lh = np
        elif number in [3,6,9]:
            answer += "R"
            rh = np
        else:
            left = abs(lh[0]-np[0]) + abs(lh[1]-np[1])
            right = abs(rh[0]-np[0]) + abs(rh[1]-np[1])
            if left < right:
                answer +="L"
                lh =np
            elif left > right:
                answer +="R"
                rh = np
            else:
                if hand == "left":
                    answer += "L"
                    lh =np
                elif hand == "right":
                    answer += "R"
                    rh = np
    return answer
# 다른풀이
def solution(numbers, hand):
    answer = ''
    location = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    left, right = [3, 0], [3, 2]
    for i in numbers:
        if i % 3 == 1:
            answer += 'L'
            left = location[i]
        elif i % 3 == 0 and i != 0:
            answer += 'R'
            right = location[i]
        else:
            l = abs(location[i][0] - left[0]) + abs(location[i][1] - left[1])
            r = abs(location[i][0] - right[0]) + abs(location[i][1] - right[1])
            if l < r:
                answer += 'L'
                left = location[i]
            elif l > r:
                answer += 'R'
                right = location[i]
            else:
                if hand == 'right':
                    answer += "R"
                    right = location[i]
                else:
                    answer += "L"
                    left = location[i]                

    return answer
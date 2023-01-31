def solution(my_str, n):
    
    # 리스트컴프리핸션 사용
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]

    # def solution(my_str, n):
    # answer = []
    # for i in range(0, len(my_str), n):
    #     answer.append(my_str[i:i+n])
    # return answer
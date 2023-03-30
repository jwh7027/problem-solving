def solution(board, moves):
    answer = 0
    ls = []
    for i in moves:
        for j in board:
            if (j[i-1] == 0):
                pass
            else:
                ls.append(j[i-1])
                j[i-1] = 0
                if len(ls) >= 2 and ls[-1] == ls[-2]:
                    ls.pop()
                    ls.pop()
                    answer += 2
                break
    return answer
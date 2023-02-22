def solution(keyinput, board):
    x1 = (board[0]-1) / 2
    x2 = -((board[0]-1) / 2)
    y1 = (board[1]-1) / 2
    y2 = -((board[1]-1) / 2 )
    answer = [0,0]
    for i in keyinput:
        if i == "left" and (answer[0] > x2):
            answer[0] -=1
        elif i == "right" and (answer[0] < x1):
            answer[0] +=1
        elif i == "up" and (answer[1] < y1):
            answer[1] +=1
        elif i == "down" and (answer[1]> y2):
            answer[1] -=1
    return answer
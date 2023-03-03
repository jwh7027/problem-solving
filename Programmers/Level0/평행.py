def solution(dots):
    dots = sorted(dots)
    answer1 = (dots[1][0] - dots[0][0], dots[1][1] - dots[0][1])
    answer2 = (dots[3][0] - dots[2][0], dots[3][1] - dots[2][1])
    a = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0]) #기울기
    b = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    if answer1 == answer2 or a == b:
        return 1
    else:
        return 0
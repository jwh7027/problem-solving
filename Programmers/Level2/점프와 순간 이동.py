def solution(n):
    result = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            result += 1

    return result
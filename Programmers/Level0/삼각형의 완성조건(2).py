def solution(sides):
    a = max(sides) - min(sides)
    b = max(sides) + min(sides)
    return b-a-1
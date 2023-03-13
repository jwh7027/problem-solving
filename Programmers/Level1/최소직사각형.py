def solution(sizes):
    row = 0
    col = 0
    for a,b in sizes:
        if a < b:
            a,b = b,a
        row = max(row,a)
        col = max(col,b)
        
    return row * col

#리스트 컴프리헨션 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
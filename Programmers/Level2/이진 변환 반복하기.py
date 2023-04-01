def solution(s):
    cnt = [0,0] # 변환 횟수, 0의 개수
    while len(s) > 1:
        cnt[1] += s.count("0")
        cnt[0] += 1
        s = bin(s.count("1"))[2:]
    return cnt
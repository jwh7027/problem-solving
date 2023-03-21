def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    cnt_0 = lottos.count(0)
    ans = 0
    for i in lottos:
        if i in win_nums:
            ans += 1
    return rank[cnt_0+ans],rank[ans]

#해시 풀이
def solution(lottos, win_nums):
    rank = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    return rank[len(set(lottos)&set(win_nums))+lottos.count(0)],rank[len(set(lottos)&set(win_nums))]
from itertools import combinations
def solution(nums):
    answer = 0
    cnt = 0
    for i in combinations(nums,3):
        answer = sum(i)
        for j in range(2,answer//2+1):
            if answer % j == 0:
                break
        else:
            cnt += 1
    return cnt
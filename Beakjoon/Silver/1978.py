n = int(input())
nums = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if nums[i] == 1: # 1은 제외
        continue
    for j in range(2,nums[i]//2+1): #구간 최소로
        if (nums[i] % j == 0):
                break
    else:
        cnt += 1
print(cnt)
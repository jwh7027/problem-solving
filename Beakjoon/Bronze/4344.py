c = int(input())
count = 0
for i in range(c):
    n = list(map(int,input().split()))
    # 학생 평균
    result = sum(n[1:]) / (len(n)-1)
    for j in n[1:]:
        #평균 넘는 학생 비율
        if (j > result):
            count += 1
        avg = count / n[0] * 100
    print(f"{avg:.3f}%")
    count = 0 # 평균 넘는 학생 수 초기화
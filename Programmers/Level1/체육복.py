def solution(n, lost, reserve):
    
    total = [1] * n
    for i in lost:
        total[i-1] -= 1
    for j in reserve:
        total[j-1] += 1
    
    for k in range(n-1):
        left = total[k]
        right = total[k+1]

        if (left,right) == (0, 2) : (total[k], total[k+1]) = (1,1)
        elif (left,right) == (2, 0) : (total[k], total[k+1]) = (1,1)
        else:
            pass
    return n - total.count(0)
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer

#넘파이 풀이
import numpy as np
def solution(arr1, arr2):
    a = np.array(arr1)
    b = np.array(arr2)
    answer = a + b
    return answer.tolist()
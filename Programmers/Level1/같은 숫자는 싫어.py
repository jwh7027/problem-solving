def solution(arr):
    stack = [-1]
    for i in range(len(arr)):
        if stack[-1] != arr[i]:
            stack.append(arr[i])
    stack.pop(0)
    return stack
    ## 슬라이싱 이용한 풀이
    stack = []
    for i in arr:
        if stack[-1:] == [i]: continue
        stack.append(i)
    return stack

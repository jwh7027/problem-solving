def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
    return [-1] if len(arr) == 1 else arr
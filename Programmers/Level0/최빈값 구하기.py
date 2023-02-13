def solution(array):
    while len(array) != 0:
        for i,d in enumerate(set(array)):
            array.remove(d)
        if i == 0: return d
    return -1
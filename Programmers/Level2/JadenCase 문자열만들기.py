def solution(s):
    s = list(s.split(' '))
    for i in range(len(s)):
        s[i] = s[i].capitalize()

    return " ".join(s)
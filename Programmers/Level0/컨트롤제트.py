def solution(s):
    s = s.split(" ")
    ls = []

    if s[0] is not s[0].isalpha():
        ls.append(int(s[0]))
    for i in range(1,len(s)):
        if s[i] == 'Z':
            ls.pop()
        else:
            ls.append(int(s[i]))
    return sum(ls)
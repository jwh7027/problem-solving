def solution(spell, dic):
    for i in dic:
        if sorted(i) == sorted(spell):
               return 1
        else:
            return 2

#집합 활용
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

# 부분함수 사용
def solution(spell, dic):
    for word in dic:
        if set(spell).issubset(set(word)):
            return 1
    return 2
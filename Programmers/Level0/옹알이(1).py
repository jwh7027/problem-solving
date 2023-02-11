from itertools import permutations
def solution(babbling):
    word = ["aya","ye","woo","ma"]
    answer = 0
    for i in babbling:
        for j in word:
            i = i.replace(j,"-",1)
        if i.replace("-","") == "":
            answer +=1
    return answer

# permutations 순열로 푸는 방법
#     answer = 0
#     ls = ["aya","ye","woo","ma"]
#     word = []

#     for i in range(1,len(ls)+1):
#         for j in permutations(ls,i):
#             word.append("".join(j))

#     for i in babbling:
#         if i in word:
#             answer +=1
#     return answer
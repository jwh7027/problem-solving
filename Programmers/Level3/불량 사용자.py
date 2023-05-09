import re
def search(idx, visit, user_id, answer, banPatterns):
    if idx == len(banPatterns):
        answer.add(visit)
        return
    for i in range(len(user_id)):
        #visit & (1 << i) 방문여부 검사
        if (visit & (1 << i)) > 0 or not re.fullmatch(banPatterns[idx], user_id[i]): continue
        # visit | (1 << i) 다음 위치 생성
        search(idx + 1, visit | (1 << i), user_id, answer, banPatterns)

def solution(user_id, banned_id):
    answer = set()
    banPatterns = [x.replace('*','.') for x in banned_id]
    search(0,0, user_id,answer,banPatterns)
    
    return len(answer)

# 다른풀이 
# from itertools import permutations
# import re
# def solution(user_id, banned_id):
#     banned = ' '.join(banned_id).replace('*','.')
#     answer = set()
    
#     for i in permutations(user_id,len(banned_id)):
#         if re.fullmatch(banned, ' '.join(i)):
#             answer.add(''.join(sorted(i)))
            
#     return len(answer)
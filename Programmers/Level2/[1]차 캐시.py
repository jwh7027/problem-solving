from collections import deque
def solution(cacheSize, cities):
    answer = 0
    stack = deque([])
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    time = 0
    if cacheSize == 0:
        time = len(cities) * 5
    else:
        for i in cities:
            if i not in stack:
                stack.append(i)
                time += 5
                if len(stack) > cacheSize:
                    stack.popleft()
            else:
                stack.remove(i) # LRU의 특징인 최근 검색 자료를 제일 앞으로 보내주기 위해 과거의 cache 지우고 
                stack.append(i) # 최근 검색 자료 추가
                time += 1
                if len(stack) > cacheSize:
                    stack.popleft()
    answer = time
    return answer
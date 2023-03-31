def solution(numbers, target):

    def DFS(numbers, target, depth):
        answer = 0
        if depth == len(numbers):
            if sum(numbers) == target:
                return 1
            else: return 0
        else:
            answer += DFS(numbers, target, depth+1)
            numbers[depth] *= -1
            answer += DFS(numbers, target, depth+1)
            return answer

    answer = DFS(numbers, target, 0)
    return answer

#BFS 풀이
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0,0))
    while queue:
        cur_sum , index = queue.popleft()

        if index == len(numbers):
            if cur_sum == target:
                answer += 1
        else:
            cur_number = numbers[index]
            queue.append((cur_sum + cur_number, index + 1))
            queue.append((cur_sum - cur_number, index + 1))
    return answer
    
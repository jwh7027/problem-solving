def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(cur_v):
        visited[cur_v] = True
        for i in range(n):
            if not visited[i] and computers[cur_v][i] == 1:
                dfs(i)

    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1
    return answer
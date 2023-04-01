from collections import deque
def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])

    def bfs(x,y):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        queue = deque()
        queue.append((x,y))
        maps[x][y] = 1
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
        return maps[row-1][col-1] if maps[row-1][col-1] > 1 else -1

    answer = bfs(0,0)
    return answer
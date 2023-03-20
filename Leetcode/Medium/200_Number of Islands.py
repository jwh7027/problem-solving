#dfs
class Solution:
    def numIslands(self,grid):
        row = len(grid)
        col = len(grid[0])
        
        def dfs(x,y):
            if x <= -1 or x >= row or y <= -1 or y >= col:
                return False
                 # 현재 노드를 아직 방문하지 않았다면
            if grid[x][y] == "1":
                # 해당 노드 방문 처리
                grid[x][y] = "0"
                # 상 하 좌 우 위치들 재귀적으로 호출
                dfs(x - 1, y)
                dfs(x, y - 1)
                dfs(x + 1 , y)
                dfs(x, y + 1)
                return True
        result = 0
        for i in range(row):
            for j in range(col):
                if dfs(i,j) == True:
                    result += 1
        return result

#bfs
from collections import deque
def numIslands(self,grid):
        number_of_islands = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def bfs(x,y):
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]

            visited[x][y] = True
            queue = deque()
            queue.append((x,y))
            while queue:
                cur_x,cur_y = queue.popleft()
                for i in range(4):
                    next_dx = cur_x + dx[i]
                    next_dy = cur_y + dy[i]
        
                    if next_dx >= 0 and next_dx <  m and next_dy >=0 and next_dy < n:
                        continue
                    if grid[next_dx][next_dy] == "0":
                        continue
                    if grid[next_dx][next_dy] == "1" and not visited[next_dx][next_dy]:
                        visited[next_dx][next_dy] == True
                        queue.append((next_dx,next_dy))
            return False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i,j)
                    number_of_islands += 1
        return number_of_islands

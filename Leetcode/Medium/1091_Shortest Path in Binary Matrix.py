from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        dx = [-1,1,-1,-1,1,1,0,0]
        dy = [0,0,-1,1,-1,1,-1,1]

        if grid[0][0] == 1: return -1

        def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            grid[x][y] = 1
            while queue:
                x,y = queue.popleft()
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if grid[n-1][n-1] == 1:
                        return -1
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = grid[x][y] + 1
                        queue.append((nx,ny))
            return grid[n-1][n-1] if grid[n-1][n-1] else -1

        res = bfs(0,0)
        return res

#다른 풀이
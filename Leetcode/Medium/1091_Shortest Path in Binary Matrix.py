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
from collections import deque

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])
    visited = [[False] * col for _ in range(row)]

    delta = [(1,0), (-1,0), (0,1), (0,-1),
             (1,1), (1,-1), (-1,1), (-1,-1)]
    
    if grid[0][0] == 1 or grid[row-1][col-1] == 1: return -1

    queue = deque()
    queue.append((0,0,1))
    visited[0][0] = True

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        #목적지에 도착했을 때 그때의 cur_len를 shortest_len에 저장
        if cur_r == row - 1 and cur_c == col - 1:
            shortest_path_len = cur_len
            break

        for dr,dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >=0 and next_r < row and next_c >=0 and next_c < col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r,next_c,cur_len + 1))
                    visited[next_r][next_c] = True

    return shortest_path_len
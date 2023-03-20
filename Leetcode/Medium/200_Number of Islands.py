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
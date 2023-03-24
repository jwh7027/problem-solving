class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)

        def dfs(cur_v):
            visited[cur_v] = True
            for i in rooms[cur_v]:
                if not visited[i]:
                    dfs(i)
        dfs(0)
        return all(visited)
    
#bfs
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)

        def bfs(cur_v):
            queue = deque()
            queue.append(cur_v)
            visited[cur_v] = True
            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if not visited[cur_v]:
                        queue.append(next_v)
                        visited[next_v] = True

        bfs(0)
        return all(visited)
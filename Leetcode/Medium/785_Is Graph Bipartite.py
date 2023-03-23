class Solution:
    def isBipartite(self, graph):
        visited = [0] * len(graph)

        def dfs(cur_v):
            if not visited[cur_v]:
                visited[cur_v] = -1

            for v in graph[cur_v]:
                if not visited[v]:
                    visited[v] = -visited[cur_v]
                    dfs(v)
                elif visited[cur_v] == visited[v]:
                    return False
            return True
        node = [x for x in range(len(graph))]
        result = all(list(map(dfs, node)))
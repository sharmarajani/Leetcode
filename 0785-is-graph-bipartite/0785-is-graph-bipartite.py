class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        Bipartite = True
        color = [-1] * len(graph)
        def dfs (graph, color, idx):
            # base
            nonlocal Bipartite
            if not Bipartite:
                return
            # logic
            for nei in graph[idx]:
                if color[nei] == -1:
                    color[nei] = 1-color[idx]
                    dfs(graph, color, nei)
                else:
                    if color[nei]==color[idx]:
                        Bipartite = False
                        return
        for i in range(len(graph)):
            if color[i]==-1:
                color[i] = 1
                dfs(graph, color, i)
        return Bipartite
        
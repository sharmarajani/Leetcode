class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        Bipartite = True
        n = len(graph)
        color = [-1] * n
        q= deque()
        for i in range(n):
            if color[i]==-1:
                color[i]=1
                q.append(i)
                while q:
                    for _ in range(len(q)):
                        ele = q.popleft()
                        for nei in graph[ele]:
                            if color[nei]==-1:
                                q.append(nei)
                                color[nei]=1-color[ele]
                            else:
                                if color[nei]== color[ele]:
                                    Bipartite = False
                                    return False
        return True

                        

        
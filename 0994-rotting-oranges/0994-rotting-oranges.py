class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m ,n = len(grid) , len(grid[0])
        q= deque()
        fresh, cnt = 0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        dirs =[[0,1], [0,-1], [1,0], [-1,0]]
        cnt=0
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for diri in dirs:
                    nr= row + diri[0]
                    nc= col + diri[1]
                    if nr<0 or nr>=m or nc<0 or nc >=n or grid[nr][nc] != 1:
                        continue
                    else:
                        grid[nr][nc]=2
                        q.append((nr, nc))
                        fresh-=1
            cnt+=1
        return cnt if fresh==0 else -1



        
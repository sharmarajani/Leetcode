class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid==None or len(grid)==0:
            return None
        q = collections.deque()
        m= len(grid)
        n=len(grid[0])
        size=0
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    size+=1
                    grid[i][j]=0
                    q.append([i,j])
                    while q:
                        row,col = q.popleft()
                        for diri in dirs:
                            nr = row + diri[0]
                            nc = col + diri[1]
                            if 0 <= nr < m and 0<=nc < n:
                                if grid[nr][nc]=="1":
                                    q.append([nr,nc])
                                    grid[nr][nc] = '0'
        return size

                    


         
        
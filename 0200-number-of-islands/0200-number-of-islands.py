class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs= [[0,1], [0,-1], [-1,0], [1,0]]
        m= len(grid)
        n = len(grid[0])
        count = 0

        def dfs ( nr, nc):
            if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == "0" :
                return 
            grid[nr][nc] = "0"
            for diri in dirs:
                r = diri[0] + nr
                c = diri[1] + nc
                dfs(r,c)
            

        for i in range(m):
            for j in range(n):
                if grid[i][j]== "1":
                    count+=1
                    dfs(i,j)
        return count

        
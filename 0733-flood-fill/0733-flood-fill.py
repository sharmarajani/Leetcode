class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val=image[sr][sc]
        m = len(image)
        n = len(image[0])
        q= collections.deque()
        q.append([sr,sc])
        dirs= [[0,1],[0,-1],[1,0],[-1,0]]
        if val ==color:
            return image
        while q:
            row, col = q.popleft()
            image[row][col]= color
            for diri in dirs:
                nr = row + diri[0]
                nc  = col + diri[1]
                if 0<=nr < m and 0<= nc < n:
                    if image[nr][nc]== val:
                        q.append([nr,nc])
        return image


        
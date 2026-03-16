class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row = len(grid)
        col = len(grid[0])
        res = []
        for j in range(col):
            cur_col = j
            for r in range(row):
                directions = grid[r][cur_col]
                next_col = cur_col + directions
                if next_col >=col or next_col < 0 or grid[r][next_col] != directions:
                    cur_col = -1
                    break
                cur_col = next_col
            res.append(cur_col)
        return res
        
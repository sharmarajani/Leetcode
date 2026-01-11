class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix==None or len(matrix)==0:
            return 0
        m, n = len(matrix), len(matrix[0])
        maxi = 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j]= min(dp[i-1][j] , dp[i][j-1] , dp[i-1][j-1])+ 1
                    maxi= max(dp[i][j], maxi)

        return maxi*maxi        
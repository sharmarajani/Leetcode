class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == None or len(matrix)==0:
            return 0
        m, n = len(matrix) , len(matrix[0])
        max_area =0
        dp =[0] * n
        def largestRectangle(dp):
            stack = []
            maxi = 0
            dp.append(0)
            # row, col = len(dp) , len(dp[0])
            for i in range((len(dp))):
                start = i
                while stack and stack[-1][0] > dp[i]:
                    val, idx = stack.pop()
                    maxi = max (maxi, val * (i-idx))
                    start = idx
                stack.append([dp[i], start])
            return (maxi)
        
        for i in range(m):
            for j in range (n):
                if matrix[i][j]=="1":
                    dp[j]= dp[j] +1
                else:
                    dp[j]=0
            max_area = max(max_area, largestRectangle(dp))
        return max_area
    
        


        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n =len(s)
        if n < 2:
            return s
        start, max_len  = 0,1
        dp =[[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n):
            for j in range(i):
                if s[i] == s[j]:
                    if i-j < 2 or dp[i-1][j+1]:
                        dp[i][j]=  True

                        if i-j+1 > max_len:
                            max_len = i-j+1
                            start = j
        return s[start : start+max_len]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board)==0:
            return False
        def dfs (board, word, idx, row, col):
            dirs= [[0,1],[1,0],[0,-1],[-1,0]]
            if idx ==len(word):
                return True
            if row >= len(board) or row <0 or col >=len(board[0]) or col < 0 or board[row][col]!=word[idx]:
                return False
            
            ch=board[row][col]
            board[row][col] = "#"
            for ndir in dirs:
                nr = ndir[0] + row
                nc = ndir[1] + col
                if dfs (board, word, idx+1, nr, nc):
                    return True
            board[row][col] = ch
            return False
            

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if dfs(board, word, 0,i,j):
                        return True
        return False    
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board) , len(board[0])
        def capture(row, col):
            if row < 0 or row == m or col < 0 or col ==n or board[row][col]!= "O":
                return
            board[row][col] = "T"
            capture(row+1, col)
            capture(row-1, col)
            capture(row, col+1)
            capture(row, col-1)

        # capture unsurrounded region O --> T
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1) or (j==0 or  j ==n-1) and board[i][j]== "O" :
                    capture(i,j)
        # cature surrounded region O --> X
        for i in range(m):
            for j in range(n):
                if  board[i][j]=="O":
                    board[i][j]= "X"
        # uncapyure unsurrounded region T --> O
        for i in range(m):
            for j in range(n):
                if  board[i][j]=="T":
                    board[i][j]="O"
                
        # capture(0,0)
        

        
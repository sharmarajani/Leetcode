class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==0:
            return 0
        colSet =set()
        posDiag = set()
        negDiag= set()
        res=[]
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            # base
            if r == n:
                copy = ["". join(r) for r in board]
                res.append(copy)
                return
            # logic
            for c in range(n):
                if c in colSet or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                # backtrack
                backtrack(r+1)
                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        print(res)
        return res



        
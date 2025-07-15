class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board[0])
        n=len(board)
        v=[[0]*m for i in range(n)]

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]  

        for i in range(n):
            for j in range(m):
                if i==0 or j==0 or i==n-1 or j==m-1:
                    if board[i][j] == "O" and (not v[i][j]):
                        q = deque([(i,j)])
                        v[i][j] = 1
                        while(q):
                            r,c = q.popleft()
                            for z in range(4):
                                nrow, ncol = r + delRow[z], c + delCol[z]
                                if (0 <= nrow < n and 0 <= ncol < m) and (not v[nrow][ncol]) and (board[nrow][ncol] == "O"):
                                        v[nrow][ncol] = 1
                                        q.append((nrow, ncol))
        ans=0
        for i in range(n):
            for j in range(m):
                if (board[i][j] == "O") and (v[i][j]==0):
                    board[i][j] = "X"
        
        
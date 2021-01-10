class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return
        m, n = len(board), len(board[0])
        
        alive = set()
        
        def checkNumLive(i, j):
            liveCount = 0
            for x, y in map(lambda a: (a[0] + i, a[1] + j), ([(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)])):
                if 0 <= x < m and 0 <= y < n:
                    if board[x][y] == 1:
                        liveCount += 1
            return liveCount
        
        for i in range(m):
            for j in range(n):
                liveCount = checkNumLive(i, j)
                if board[i][j] == 1:              
                    if 2 <= liveCount <= 3:
                        alive.add((i, j))
                else:
                    if liveCount == 3:
                        alive.add((i, j))
        
        for i in range(m):
            for j in range(n):
                if (i, j) in alive:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
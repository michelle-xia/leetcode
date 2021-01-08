class Solution:
    def isValidSudoku(self, board):
        if board is None:
            return
        def checkRows():
            for i in range(len(board)):
                cache = set()
                for j in range(len(board[i])):
                    if board[i][j] != ".":
                        if board[i][j] in cache:
                            return False
                        else:
                            cache.add(board[i][j])
            return True
        
        def checkCols():
            for i in range(len(board[0])):
                cache = set()
                for j in range(len(board)):
                    if board[j][i] != ".":
                        if board[j][i] in cache:
                            return False
                        else:
                            cache.add(board[j][i])
            return True
        
        def checkSquares():
            for i in range(3):              
                rowstart = 3 * i
                for j in range(3):                   
                    colstart = 3 * j
                    cache = set()
                    for l in range(3):
                        row = rowstart + l
                        for k in range(3):
                            col = colstart + k
                            if board[row][col] != ".":
                                if board[row][col] in cache:
                                    return False
                                else:
                                    cache.add(board[row][col])
            return True
                    
        return checkRows() and checkCols() and checkSquares()
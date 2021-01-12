class Solution:
    def exist(self, board, word):
        if board is None or len(board) == 0 or len(word) == 0:
            return False
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j, letter, path):
            if len(path) == len(word):
                return True
            
            for a, b in [(x, y) for (x, y) in ((i+1, j), (i, j+1), (i-1, j), (i, j-1))if 0<=x<m and 0<=y<n]:
                if board[a][b] == word[letter] and (a, b) not in path:
                    path.add((a, b))
                    if dfs(a, b, letter + 1, path):
                        return True
                    path.discard((a, b))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1, {(i, j)}):
                        return True
        return False
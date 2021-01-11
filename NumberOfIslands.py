# BFS solution
class Solution:
    def numIslands(self, grid):
        
        if grid is None or len(grid) == 0:
            return 0
        
        visited = set()
        islandCount = 0
        m, n = len(grid), len(grid[0])
        
        def bfs(i, j):
            q = [(i, j)]
            
            while q:
                a, b = q.pop(0)
                for x, y in map(lambda k: (k[0] + a, k[1] + b), ([(0,1), (1, 0), (-1, 0), (0, -1)])):
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                        visited.add((x, y))
                        if grid[x][y] == "1":
                            q.append((x, y))
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if grid[i][j] == "1":
                        bfs(i, j)
                        islandCount += 1
                               
        return islandCount

# DFS solution
class Solution2:
    def numIslands(self, grid):
        
        if grid is None or len(grid) == 0:
            return 0
        
        islandCount = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for (a, b) in [(x, y) for (x, y) in ((i + 1, j), (i, j + 1), (i-1, j), (i, j-1)) if 0 <= x < m and 0 <= y < n]:
                dfs(a, b)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islandCount += 1
                            
        return islandCount
class Solution:
    def pacificAtlantic(self, matrix):
        if matrix is None or len(matrix) == 0:
            return
        m, n = len(matrix), len(matrix[0])
        pac = [(0, i) for i in range(n)] + [(j, 0) for j in range(m)]
        atl = [(m - 1, i) for i in range(n)] + [(j, n - 1) for j in range(m)]
        def bfs(q):
            visited = set()    
            while q:
                i, j = q.pop(0)
                visited.add((i, j))   
                for x, y in map(lambda n: (n[0] + i, n[1] + j), ([(0, 1), (1, 0), (0, -1), (-1, 0)])):
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and matrix[x][y] >= matrix[i][j]:
                        q.append((x, y))
            return visited
                
        return bfs(pac) & bfs(atl)
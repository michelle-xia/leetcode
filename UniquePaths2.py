from functools import lru_cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        @lru_cache
        def getPaths(i, j):
            if i >= len(obstacleGrid) or j >= len(obstacleGrid[0]) or obstacleGrid[i][j] == 1:
                return 0
            if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                return 1 
            return getPaths(i + 1, j) + getPaths(i, j + 1)
        
        return getPaths(0, 0)
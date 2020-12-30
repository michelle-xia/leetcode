class Solution:
    def minPathSum(self, grid):
        if grid is None or len(grid) == 0:
            return
        
        dp = grid[:][:]
        
        for i in range(1, len(dp)):
            dp[i][0] = dp[i - 1][0] + dp[i][0]
        
        for i in range(1, len(dp[0])):
            dp[0][i] = dp[0][i - 1] + dp[0][i]
            
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])
                
        return dp[len(dp) - 1][len(dp[0]) - 1]
        
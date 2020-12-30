class Solution:
    def uniquePaths(self, m, n):
        
        numerator = 1
        denominator = 1
        
        # i = 1
        k = min(m, n) - 1
        
        for i in range(k):
            numerator *= (m + n - 2) - i
            denominator *= k - i
        return numerator // denominator
        
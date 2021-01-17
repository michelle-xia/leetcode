class Solution:
    def lengthOfLIS(self, nums):
        outerBound = len(nums) + 1
        dp = [0] * outerBound
        res = 0
        for j in range(1, outerBound):
            dp[j] = 1
            for i in range(1, j):
                if nums[j-1] > nums[i-1]:
                    dp[j] = max(dp[j], dp[i] + 1)
            res = max(res, dp[j])
        return res
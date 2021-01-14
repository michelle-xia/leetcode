class Solution:
    def maxProfit(self, prices):
        if prices is None or len(prices) < 2:
            return 0
        buy = prices[0]
        profit = prices[1] - prices[0]
        for i in range(1, len(prices)):
            if prices[i-1] < buy:
                buy = prices[i-1]
            if profit < prices[i] - buy:
                profit = prices[i] - buy
        return profit if profit > 0 else 0
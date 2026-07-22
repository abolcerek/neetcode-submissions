class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minB = prices[0]
        for i in prices:
            profit = max(profit, i - minB)
            minB = min(minB, i)
        return profit
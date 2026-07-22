class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = prices[0]

        for i in prices:
            profit = max(profit, i - minBuy)
            minBuy = min(minBuy, i)
        return profit

        
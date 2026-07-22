class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        profit = 0

        for i in prices:
            profit = max(profit, i - minbuy)
            minbuy = min(minbuy, i)
        return profit
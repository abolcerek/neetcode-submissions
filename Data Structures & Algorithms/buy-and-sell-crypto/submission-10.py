class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Input: prices = [10,1,5,6,7,1]
        # min buy tracker
        # profit = abs(minbuy - price)
        # profit = max(profit, whatever)
        profit = 0
        min_buy = float('inf')
        for price in prices:
            min_buy = min(min_buy, price)
            curr_profit = min_buy - price
            if curr_profit <= 0:
                profit = max(profit, abs(curr_profit))
            else:
                continue
        return profit





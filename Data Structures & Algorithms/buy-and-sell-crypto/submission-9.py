class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #profit at min 0, at best i - j

        #compare i to i + 1 i + 2 i..n
            #record profit and set it to be the max between prices[i] - prices[i + j]
        

        profit = 0
        minbuy = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minbuy:
                minbuy = prices[i]
            profit = min(0, minbuy - prices[i])
            if profit < maxprofit:
                maxprofit = profit
        return -maxprofit 


        # prices = [10, 1, 5, 6, 7, 1]

        #minbuy = 7
        #profit = 
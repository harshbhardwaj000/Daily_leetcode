class Solution(object):
    def maxProfit(self, prices):
        low_price= float("inf")
        max_profit=0
        for price in prices:
            if price < low_price:
                low_price = price
            else:
                profit = price - low_price
                max_profit = max(max_profit , profit)
        return max_profit
            
        
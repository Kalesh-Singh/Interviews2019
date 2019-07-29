class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        # Solution 1 - Dynamic Programming
        # Keep track of running min price and profit

        min_price = float('inf')
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = max(profit, price - min_price)

        return profit

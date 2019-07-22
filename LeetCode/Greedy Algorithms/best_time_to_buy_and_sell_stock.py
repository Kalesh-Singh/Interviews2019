class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        # Solution 1 - Intuitive Approach
        # O(n) Time O(1) Space
        # if not prices:
        #     return 0
        # i = j = 0
        # profit = 0
        # l = len(prices) - 1
        # while i < l:
        #     while i < l and prices[i] > prices[i+1]:
        #         i += 1
        #     j = i
        #     while j < l and prices[j] < prices[j+1]:
        #         j += 1
        #     if i < j:
        #         profit += prices[j] - prices[i]
        #     i = j + 1
        # return profit

        # Solution 2 - Greedy Approach
        # O(n) Time, O(1) Space
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit
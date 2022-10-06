"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a
single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        temp_profit = 0
        buy_day = 0
        for i in range (len(prices)-1):
            if(prices[buy_day] > prices [i+1]):
                buy_day = i+1
            temp_profit = prices[i+1] - prices[buy_day]
            if(max_profit < temp_profit):
                max_profit = temp_profit

        return max_profit

test = Solution.maxProfit(Solution, [7,1,5,3,6,4])
print(test)
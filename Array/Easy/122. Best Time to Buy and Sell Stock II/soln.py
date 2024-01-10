#subtracting every consecutive decreasing numbers will in turn give the max profit
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                max += prices[i] - prices[i-1]
        return max

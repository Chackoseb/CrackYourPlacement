#two pointers left and right used : left - buy, right - sell
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0, 1
        max = 0
        k= len(prices)
        while r < k:
            current = prices[r] - prices[l]
            if(current > max):
                max = current
            if prices[l] > prices[r]:
                l = r
            
            r += 1
        if max <= 0:
            return 0
        else:
            return max

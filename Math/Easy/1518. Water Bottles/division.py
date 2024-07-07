class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        count_drinkable = numBottles
        empty = 0
        while(numBottles >= numExchange):
            addToCount = numBottles // numExchange
            count_drinkable += addToCount
            empty = numBottles % numExchange
            numBottles = addToCount
            numBottles += empty
        return count_drinkable

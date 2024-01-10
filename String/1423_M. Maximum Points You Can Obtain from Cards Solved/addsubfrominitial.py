class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        maxscore = 0
        result = 0
        l = k - 1
        r = len(cardPoints) - 1
        for j in range(k): #calculate sum of first k elements
            maxscore += cardPoints[j]
            result = maxscore
        while(k): #slide the window
            k -= 1
            maxscore -= cardPoints[l] 
            maxscore += cardPoints[r]
            if maxscore > result:
                result = maxscore
            l -= 1
            r -= 1
        return result

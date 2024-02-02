class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, 10):
            num = i
            nextnum = i+1
            while num <= high and nextnum <= 9:
                num = num*10 + nextnum
                if low <= num <= high:
                    res.append(num)
                nextnum += 1

        res.sort()
        return res

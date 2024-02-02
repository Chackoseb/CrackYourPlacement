class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        digits = "123456789"
        result = []
        len_low = len(str(low))
        len_high = len(str(high))
        for i in range(len_low, len_high+1):
            for j in range(0, 10-i):
                num = int(digits[j: j+i])
                if num >= low and num <= high:
                    result.append(num)
        return result

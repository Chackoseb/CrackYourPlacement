class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = s.split() #give noparameters so all kinds of spaces avoided
        return len(ls[-1])

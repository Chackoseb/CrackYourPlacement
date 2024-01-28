class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        leng = len(s)
        r = leng - 1
        while l <= r:
            while not s[l].isalnum() and l < leng-1:
                l += 1
            while not s[r].isalnum() and r > l:
                r -= 1
            if s[l].lower() != s[r].lower() and r >= l:
                return False
            l += 1
            r -= 1
        return True

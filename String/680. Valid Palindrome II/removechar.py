#tries removing character pointed by left pointer and checks if palindrome. if not, tries the same by removing the character pointed by right pointer
#compares entire string after removing the character

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                copystr = s[:l] + s[l+1:]
                if copystr == copystr[::-1]:
                    return True
                else:
                    copystr = s[:r] + s[r+1:]
                    if copystr == copystr[::-1]:
                        return True
                    else:
                        return False
        return True

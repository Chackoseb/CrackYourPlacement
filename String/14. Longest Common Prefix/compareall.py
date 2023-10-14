lass Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        n = len(strs[0])
        for i in range(n):
            for words in strs:
                if i == len(words) or words[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

'''The idea is to add ')' only after valid '('
We use two integer variables left & right to see how many '(' & ')' are in the current string
If left < n then we can add '(' to the current string
If right < left then we can add ')' to the current string'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(left, right, s):
            if len(s) == 2 * n:
                res.append(s)
                return

            if left < n:
                backtrack(left + 1, right, s + '(')

            if right < left:
                backtrack(left, right + 1, s + ')')

        res = []
        backtrack(0, 0, '')
        return res

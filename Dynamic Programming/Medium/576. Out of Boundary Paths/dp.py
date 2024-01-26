class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        rows, cols = m, n
        mod = 10**9 + 7
        cache = {}
        def dfs(r, c, moves):
            if (r < 0 or r == rows or
                c < 0 or c == cols):
                return 1

            if moves == 0:
                return 0

            if (r, c, moves) in cache:
                return cache[(r, c, moves)]

            cache[(r, c, moves)] = (
                (dfs(r+1, c, moves-1) +
                dfs(r-1, c, moves-1)) % mod +
                (dfs(r, c+1, moves-1) +
                dfs(r, c-1, moves-1))
            ) % mod

            return cache[(r, c, moves)]

        return dfs(startRow, startColumn, maxMove)

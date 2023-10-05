#two pointers left and right used - initialised to first and last element
#calculate area and check with previous values
#the pointer to smaller height value updated - if value at l smaller, increment l. else decrement r
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height)-1
        while(l<r):
            area = (r - l) * min(height[l], height[r])
            res = max(area, res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

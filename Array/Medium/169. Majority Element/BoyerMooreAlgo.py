# check video https://youtu.be/7pnhv842keE?si=h4OY8ZfckJbekUdQ
# Time : O(n)  Space: O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        val = nums[0]
        for n in nums:
            if n == val:
                count += 1
            else:
                count -= 1
            if count < 0:
                count = 0
                val = n
        return val

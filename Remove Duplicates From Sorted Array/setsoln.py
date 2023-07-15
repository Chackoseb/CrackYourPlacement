class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(nums)
        nums[:]=sorted(set(nums))
        return len(nums)

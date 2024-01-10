class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls = []
        nums.sort()
        l = len(nums)
        for i in range(1, l):
            if nums[i] == nums[i-1]:
                ls.append(nums[i])
        return ls

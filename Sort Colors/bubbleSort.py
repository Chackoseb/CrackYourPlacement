class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range (n):
            for j in range (i+1,n):
                if nums[i]>nums[j]:
                    t=nums[j]
                    nums[j]=nums[i]
                    nums[i]=t

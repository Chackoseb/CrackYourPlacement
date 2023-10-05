class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(0,n):
            k=nums[i]
            for j in range(i+1,n):
                if(k==nums[j]):
                    return k

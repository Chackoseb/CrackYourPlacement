class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ls = []
        k = len(nums)
        for i in range(0, k):
            for j in range(i+1,k):
                if nums[i] + nums[j] == target:
                    ls.insert(0,i)
                    ls.insert(1,j)
        return ls

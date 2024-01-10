#good solution using 2 pointers

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0  #left pointer
        for r in range(len(nums)): #incrementing right pointer each time
            if nums[r] != 0: #when non zero value encountered in right pointer, it is swapped with left pointed element
                nums[r], nums[l] = nums[l], nums[r]
                l+=1

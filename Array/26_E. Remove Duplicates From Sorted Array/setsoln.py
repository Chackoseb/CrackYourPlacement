class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(nums)
        nums[:]=sorted(set(nums))
        return len(nums)
        
 '''Common Wrong Answers:
	nums = sorted(set(nums))
	return len(nums)
 nums =  doesn't replace elements in the original list.
nums[:] = replaces element in place

In short, without [:], we're creating a new list object, which is against what this problem is asking for:
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.'''

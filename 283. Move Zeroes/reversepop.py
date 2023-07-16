#when 0 is encountered, it is popped and appended to the end of list

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                count += 1

        for i in range(count):
            nums.append(0)


'''
If we dp this from first to last order,
when you call nums.pop(i), it modifies the list by removing the element at index i.
However, this changes the length of the list, causing the loop to go out of range.

To fix this issue, you can iterate over the list in reverse order. 
This way, when you remove an element, it won't affect the iteration of elements that you haven't processed yet.
'''

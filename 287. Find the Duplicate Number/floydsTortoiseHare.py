class Solution(object):
    def findDuplicate(self, nums):
        
        slow = nums[0]
        fast = nums[0]

        # Move pointers until they meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Reset slow pointer to the beginning
        slow = nums[0]

        # Move both pointers until they meet again
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # Return the repeated number
        return slow

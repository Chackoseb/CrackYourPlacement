#use hashmap to keep count and end when any count > n//2
# Time : O(n)  Space : O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        l = len(nums)//2
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

            if hashmap[n] > l:
                return n

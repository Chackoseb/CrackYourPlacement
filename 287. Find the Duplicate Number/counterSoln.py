class Solution(object):
    def findDuplicate(self, nums):
        c = Counter(nums)
        for k,v in c.items():
            if v > 1:
                return k

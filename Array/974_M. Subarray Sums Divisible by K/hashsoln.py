#create a hashtable with key as the mod value of each element and value as occurance of the particular mod value
#on traversal of list, if encountered a mod value that is already in hashmap,
#then add the count of the mod value to the result and increment it by one
#refer : https://youtu.be/p2UDld3rM_Q
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        preSum = 0
        hashmap = {0 : 1}
        for i in nums:
            preSum += i
            modval = preSum % k
            if modval in hashmap:
                result += hashmap[modval]
                hashmap[modval] += 1
            else:
                hashmap[modval] = 1

        return result

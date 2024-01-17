class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashmap = {}
        setmap = set()
        for el in arr:
            if el in hashmap:
                hashmap[el] += 1
            else:
                hashmap[el] = 1
        for i in hashmap.values():
            setmap.add(i)

        if len(setmap) == len(hashmap):
            return True
        else:
            return False

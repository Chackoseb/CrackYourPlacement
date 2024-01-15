#used a set to track all teams
#used a hashmap to check count or wins
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        hashcheck = {}
        setkeep = set()
        answer1 = []
        answer2 = []
        res = []

        for i, j in matches:
            setkeep.add(i)
            setkeep.add(j)

        for i in matches:
            if i[1] in hashcheck:
                hashcheck[i[1]] += 1
            else:
                hashcheck[i[1]] = 1

        for i in setkeep:
            if i not in hashcheck:
                answer1.append(i)
            elif hashcheck[i] == 1:
                answer2.append(i)

        answer1.sort()
        answer2.sort()

        res.append(answer1)
        res.append(answer2)
        return res

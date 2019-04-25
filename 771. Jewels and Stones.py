class Solution(object):
    def numJewelsInStones(self, J, S):
        J = set(J)
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count

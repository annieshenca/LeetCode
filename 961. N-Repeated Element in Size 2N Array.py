class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # h = set()
        # for i in A:
        #     if i in h:
        #         return i
        #     h.add(i)
        # return None
        
        # Use built-in sort() with run time nlogn
        A.sort()
        for i in range(len(A)):
            if A[i] == A[i+1]:
                return A[i]

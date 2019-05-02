from collections import Counter

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        # We actually only need to use Counter on the first word in A.
        a = Counter(A[0])
        
        # Compare to the rest of the As and union. The desired result
        # will be the leftovers.
        for i in A[1:]:
            a &= Counter(i)
            
        # Return the leftovers in list form.
        return list(a.elements())

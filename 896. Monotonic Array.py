class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        l = len(A)
        if l <= 2:
            return True
        
        isInceasing  = False
        isDecreasing = False
        
        for i in range(1, l):
            if A[i] > A[i-1]:
                isInceasing = True
                
            elif A[i] < A[i-1]:
                isDecreasing = True
        
        # If both boolean variables were modified, that means the numbers
        # were not going one direction in increasing or decreasing.
        if isInceasing and isDecreasing:
            return False
        
        return True
    
    # Runtime = O(l) with l meaning the length of the list A
    # Space = O(1) only used a few variables. No specific data structure.

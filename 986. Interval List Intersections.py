class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0 # Cursor for A
        j = 0 # Cursor for B
        result = []
        
        la = len(A)
        lb = len(B)
        
        while i < la and j < lb:
            # Set variables to make everything easier to look at.
            # As well as to keep my sanity. s for start. e for end.
            As = A[i][0]
            Ae = A[i][1]
            Bs = B[j][0]
            Be = B[j][1]
            
            if As > Be:
                j += 1
            elif Bs > Ae:
                i += 1
            else:
                result.append( [ max(As, Bs) , min(Ae, Be)] )
                if Ae > Be:
                    j += 1
                else:
                    i += 1
        return result

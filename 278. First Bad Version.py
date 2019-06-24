# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Use binary search!
        s = 0   # start
        e = n-1 # end
        
        while s <= e:
            # Find mid point from start to end
            mid = s + (e-s)/2
            
            # If current version is bad, then move to the left by changing the value of 'end'.
            if isBadVersion(mid):
                e = mid - 1
            # Otherwsie, change start value.
            else:
                s = mid + 1
        
        return s

# Runtime = O(logn) because of binary search
# Space = O(1)

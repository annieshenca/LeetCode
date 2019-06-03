class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        length = len(nums)
        result = [1]*length
        cur = 1
        
        # The first for-loop does multiply from left to right.
        # All while skipping its own value.
        for i in range(length):
            result[i] = cur
            cur = cur * nums[i]
        
        print "Before ", result
        
        # Reset the curser back to 1
        cur = 1
        
        # The second for-loop does the same as first loop,
        # but from right to left, to finish the complete
        # product of each index.
        # Iterate backwards and stop at -1 index.
        for i in range(length-1, -1 ,-1):
            result[i] = result[i] * cur
            cur = cur * nums[i]
        
        print "After ", result
        
        return result

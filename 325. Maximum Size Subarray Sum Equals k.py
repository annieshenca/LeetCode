class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # We want the dictionary to be: {key=sum(), value=i}
        # This is so whenever the variable total == 0, it wouldn't
        # overwrite the -1. We want to keep the values consecutive.
        table = {0:-1}
        total = 0 # The sum of all numbers in nums
        ans   = 0 # the max size subarray
        
        for i in range(len(nums)):
            print "On ", nums[i]
            total += nums[i]
            
            if total not in table:
                print nums[i], " is not in table. Now adding"
                table[total] = i
            
            remain = total - k
            
            # Trying to find if there's a subarray with sum of k, and
            # table[remain] has the staring index of that subarray.
            # Therefore, i - table[remain] is the length of the subarray!
            if remain in table:
                ans = max(ans, i - table[remain])
                print "ans is now ", ans
        return ans

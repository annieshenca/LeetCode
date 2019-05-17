class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # In Python, 0 is False, and 1 is True.
        # This variable would be -1 if x < 0 is True, and be 1 if x < 0 is False.
        positiveOrNegative = [1, -1][x < 0]
        
        # Turn x into string, invert the numbers, then change back to int, and
        # multiply by if the integer was originally positive or negative.
        result = positiveOrNegative * int( str(abs(x))[::-1] )
        
        # Due to the nature of 32-bit signed integer range, if the result is within
        # the range, then return result. Else, return 0
        return result if 2**31 > result > (-2)**31 else 0

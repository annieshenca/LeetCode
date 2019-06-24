class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        # Approach 1:
        #   Keep subtracting the divisor from divident until 
        #   divident becomes less than divisor.
        
        # Negative or not?
        sign = 1
        if dividend * divisor < 0:
            sign = -1
        
        # Update the values to be all positive in case one
        # is a negative value.
        dividend = abs(dividend)
        divisor  = abs(divisor)
        
        output = 0
        while dividend >= divisor:
            output += 1
            dividend -= divisor
        
        return output * sign

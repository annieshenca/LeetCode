class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Define a dictionary for the Symbols to Values
        symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Travel backwards from the end of the string to the front.
        # This will allow for easier addition/deduction.
        result = 0
        prev = 0
        for i in s[::-1]:
            # If the previous element was greater than current element, then this means
            # the int result should minus this current element.
            if prev > symbol[i]:
                result -= symbol[i]
            # Otherwise, keep adding.
            else:
                result += symbol[i]
            # Reset what the previous element is.
            prev = symbol[i]
        
        return result

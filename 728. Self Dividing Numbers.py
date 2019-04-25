class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Store results into a list for return.
        result = []
        
        # Iterate through all numbers in range.
        for i in range(left, right+1):
            flag = True
            copy = i
            
            # Instead of type-casting from string to int everytime,
            # which causes more time usage, we use % to get each number
            # and inspect each digit level.
            while copy != 0:
                # Flag = Flase when the number has a 0 in it.
                if (copy % 10 == 0) or (i % (copy%10) != 0):
                    flag = False
                    copy = 0 # Stops the while loop from going.
                copy = copy / 10
            # If the number is self-divide-able, then append to result.
            if flag == True:
                result.append(i)

        return result

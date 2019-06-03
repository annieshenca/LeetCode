from collections import Counter

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        # Use Counter to quickly make a hash table on all the characters exist in string T.
        count = Counter(T)
        result = ""
        
        # Add in all the important characters in S into the result string first,
        # and after each insert(as many times as it exists in T), delete the
        # character from the dictionary.
        for s in S:
            result += (s*count[s])
            del count[s]
        
        # Now, add the rest of the characters left in T into the result string.
        for char, num in count.items():
            result += (char*num)
        
        return result

        """
        Run Time: O(n)
            - The Counter() is a subclass of dict(), so it causes O(n) for creation, and
            O(1) for look ups, just as dict().
            - The rest two for loops are O(n) as well.
            - Therefore, O(n) total. 
        """

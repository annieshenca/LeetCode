'''
Given the following vectors (arbitrary numbers):

A: [1, 1, 4, 4, 4, 4, 7, 7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
B: [2, 2, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
Suggest a more memory-efficient representation of these vectors.
With the vectors represented as suggested in (1), write a function to calculate the dot product of two vectors.
Additional information:

The vectors are guaranteed to contain a large number of duplicate values, similar to the example given above.
'''

def compress (l) :
    result = [] # The list to append lists and function return.
    count = 0
    curr = None # Pointing at current list element.

    
    for i in range(len(l)):
        # curr is None at the beginning of the function call. No element will be None in list.
        if curr is None:
            curr = l[i]
            count += 1

        # If list element is now different, the append what we counted before into the result
        # list, and reset curr value and count value.
        elif curr != l[i]:
            result.append([count, curr])
            curr = l[i]
            count = 1
        
        # Otherwsie, that curr is the same as current element, then just increment counter.
        else:
            count += 1

    # Once reached the end of the list, the last set was not appended into result list,
    # so append now.
    result.append([count, curr])
    
    # Return desired result list.
    return result


# Driver code
test1 = [1, 1, 4, 4, 4, 4, 7, 7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
test2 = [1, 1, 4, 4, 4, 4, 7, 7, 7, 7, 7]
print (compress(test1))
print (compress(test2))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        result = dummy = ListNode(0)
        
        while l1 and l2:
            if l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            else:
                # If l2.val > l1.val OR both same values
                dummy.next = l1
                l1 = l1.next
                
            # Since dummy right now is pointing at either l1 or l2 value, now, update
            # it to the next spot (which is None) for the next loop to update.
            dummy = dummy.next
            
        # In case that there's leftovers in l1 or l2 (not both at the same time),
        # add the rest of that Linked List into the back of dummy.
        dummy.next = l1 or l2
        
        # Return the result.next, instead of just result, to skip the 0.
        return result.next

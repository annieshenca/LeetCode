# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Create new blank List
        temp = cur = ListNode(0)
        carry = 0
        
        # If either is empty, just return the other.
        if not l1:
            return l2
        if not l2:
            return l1
        
        # Loop until both l1 and l2 are both at end, and carry is added
        # to the end as well.
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry = carry/10
        
        # Return the head of the new result ListNode.
        return temp.next
        

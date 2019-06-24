# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # Keep track of a stack infurstracture.
        self.stack = []
        
        # Append the 'smallest' aka 'leftest' nodes into stack first
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        # Obtain the smallest node in the stack, which would be the last
        # element in the stack.
        node = self.stack.pop()
        n = node.right
        
        while n:
            # Keep adding the left 'smallest' nodes into stack
            self.stack.append(n)
            # Keep going until n = None
            n = n.left
        
        # Once all the nodes are added into the stack, now we return the
        # original 'smallest' node we were on!
        return node.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        # There would be no next if stack is empty.
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

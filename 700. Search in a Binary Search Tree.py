# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        # Go to left branch
        if root.val > val :
            return self.searchBST(root.left, val)
        # Go to right branch
        elif root.val < val:
            return self.searchBST(root.right, val)
        
        # Root == val
        return root

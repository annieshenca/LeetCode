# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        
        # Reached a None leaf
        if root is None:
            return None
        
        # If root.val is greater than R, then the wanted tree nodes are on the left
        # side of the tree.
        if root.val > R:
            return self.trimBST(root.left, L, R)
        
        # Else, to the right side of the tree.
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        
        # Else, trim both sides of the tree.
        else:
            root.left  = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        
        return root

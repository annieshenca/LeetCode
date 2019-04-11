# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Set upper bound to infinite and lower bound to negative infinite.
        return self.checkBST(root, float("-inf"), float("inf"))
        
    def checkBST(self, node, left, right):
        # Know when you reach the end leafs with no children.
        if not node:
            return True
        
        # If node has any children that violates the binary tree rule.
        if not (left < node.val < right):
            return False
            
        # Recurse through the whole tree, checking all left and right nodes.
        return ( self.checkBST(node.left, left, node.val) and self.checkBST(node.right, node.val, right) )




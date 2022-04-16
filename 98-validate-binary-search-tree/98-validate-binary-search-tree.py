# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidWithsymbol(root, minimum, maximum):
            #base case
            if not root: return True
            if minimum and minimum.val >= root.val:
                return False
            if maximum and maximum.val <= root.val:
                return False
            return isValidWithsymbol(root.left, minimum, root) and isValidWithsymbol(root.right, root, maximum)
        return isValidWithsymbol(root, None, None)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root.val==val:
            return root
        if root.left!=None:
            lt=self.searchBST(root.left,val) 
            if lt != None:
                return lt
        if root.right!=None:
            rt= self.searchBST(root.right,val)
            if rt != None:
                return rt
        #return None
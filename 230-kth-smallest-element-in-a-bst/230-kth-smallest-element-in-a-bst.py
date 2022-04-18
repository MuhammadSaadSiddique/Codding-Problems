# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def addvals(stack:list, root: Optional[TreeNode]):
            if root!= None:
                stack.append(root.val)
                addvals(stack,root.left)
                addvals(stack,root.right)
        st=[]
        addvals(st,root)
        
        st.sort()
        return st[k-1]
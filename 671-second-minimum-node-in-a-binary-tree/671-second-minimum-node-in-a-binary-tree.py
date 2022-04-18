# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def addvals(stack:list, root: Optional[TreeNode]):
            if root!= None:
                if root.val not in stack:
                    stack.append(root.val)
                addvals(stack,root.left)
                addvals(stack,root.right)
        st=[]
        addvals(st,root)
        
        st.sort()
        
        return st[1] if len(st)>1 else -1
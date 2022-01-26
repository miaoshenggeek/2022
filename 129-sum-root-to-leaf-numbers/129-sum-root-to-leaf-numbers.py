# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root,cur=0):
            nonlocal res
            if not root:return 
            cur=cur*10+root.val
            if not root.left and not root.right:
                res+=cur
            else:
                helper(root.left,cur)
                helper(root.right,cur)
        res=0
        helper(root)
        return res
            
        
            
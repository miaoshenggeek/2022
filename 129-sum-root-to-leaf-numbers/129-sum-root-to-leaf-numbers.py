# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root,num):
            nonlocal res
            num=num*10+root.val
            if root.left:helper(root.left,num)
            if root.right:helper(root.right,num)
            if not root.left and not root.right:
                res+=num
        res=0
        helper(root,0)
        return res
            
        
            
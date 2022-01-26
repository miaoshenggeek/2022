# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root,t):
            if not root:
                return False
            t-=root.val
            if not root.left and not root.right and t==0:
                return True
            return helper(root.left,t) or helper(root.right,t)
        return helper(root,targetSum)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            nonlocal res
            if not root.left and not root.right:
                res+=1
                return True
            is_uni=True
            if root.left:
                is_uni=helper(root.left) and is_uni and root.left.val==root.val
            if root.right:
                is_uni=helper(root.right) and is_uni and root.right.val==root.val
            res+=is_uni
            return is_uni
            
        if not root: return 0
        res=0
        helper(root)
        return res
        
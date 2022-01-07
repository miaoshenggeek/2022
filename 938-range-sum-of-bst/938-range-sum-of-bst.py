# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root,l,h):
            if not root:return
            if l<=root.val<=h:
                res.append(root.val)
                helper(root.right,l,h)
                helper(root.left,l,h)
            if root.val<l:helper(root.right,l,h)
            if root.val>h:helper(root.left,l,h)
        res=[]
        helper(root,low,high)
        return sum(res)
            
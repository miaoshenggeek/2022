# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        #find smallest leaf or shortest path with same leaf and node
        def helper(root,path):
            nonlocal res
            path=chr(root.val+ord("a"))+path
            if root.left: helper(root.left,path)
            if root.right:helper(root.right,path)
            if not root.left and not root.right and res>path:
                res=path
        res="z"*8500
        helper(root,"")
        return res
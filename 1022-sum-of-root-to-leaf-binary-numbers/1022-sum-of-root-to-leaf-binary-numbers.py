# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(root,path):
            nonlocal res
            if not root:
                return
            path+=str(root.val)
            if path and not root.left and not root.right:
                #print(path)
                res+=int(path,2)
                
            if root.left:helper(root.left,path)
            if root.right:helper(root.right,path)
            
            
        res=0
        path=""
        helper(root,path)
        return res
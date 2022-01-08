# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,path):
            nonlocal res
            if not root:return
            path=path*10+root.val
                          
            dfs(root.left,path)    
            dfs(root.right,path)
            
            if not root.right and not root.left:
                res+=path
            
        path=0
        res=0
        dfs(root,path)
        return res
            
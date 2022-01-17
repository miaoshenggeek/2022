# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, node: Optional[TreeNode]) -> int:
        if node:
            if node.left:
                if not node.left.left and not node.left.right:
                    self.rt+=node.left.val
                self.sumOfLeftLeaves(node.left)

            if node.right:
                self.sumOfLeftLeaves(node.right)
            
        return self.rt
        
    def __init__(self):
        self.rt=0
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        #at the end of each recursive loop, return the longest length using that node 
        #as the root so that the node's parent can potentially use it in its longest path computation.
        self.longest = 0
        def traverse(node, parent_val):
            if not node:
                return 0
            left, right = traverse(node.left, node.val), traverse(node.right, node.val)
            self.longest = max(self.longest, left + right)
            return 1 + max(left, right) if node.val == parent_val else 0
        traverse(root, None)
        return self.longest
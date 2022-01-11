# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.max_sum = None
    
    def recursive_sum(self, node):
        if node:
            max_sum_left = self.recursive_sum(node.left)
            node_val = node.val
            max_sum_right = self.recursive_sum(node.right)
            
            max_sum_node = max(node_val, node_val + max_sum_left, node_val + max_sum_right)
            self.max_sum = max(self.max_sum, max_sum_node, node_val + max_sum_left + max_sum_right)
            
            return max_sum_node
        return 0

    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # SOL1: Recursive Solution
        # TC = O(N) and SC = O(N) if tree is left skewed (O(logN) if tree balanced)
        self.max_sum = root.val
        self.recursive_sum(root)
        
        return self.max_sum
            
            
        
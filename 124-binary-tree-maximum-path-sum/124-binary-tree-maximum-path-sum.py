# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
            # naive: traverse once to make adjacency list, then find max subgraph
            # leveraging subtrees...
            # recurse down until leaf
            # go up, return max(root,left+root,right+root) BUT check left, right, root+left+right against global max
            max_sum = float('-inf')

            def maxPathSumSubtree(root: Optional[TreeNode]) -> int:
                if not root.left and not root.right:
                    return root.val
                left_val = maxPathSumSubtree(root.left) if root.left else float('-inf')
                right_val = maxPathSumSubtree(root.right) if root.right else float('-inf')
                dfs_max = max(root.val, left_val + root.val, right_val + root.val)

                nonlocal max_sum
                max_sum = max(max_sum, dfs_max, left_val, right_val, root.val + left_val + right_val)

                return dfs_max

            return max(maxPathSumSubtree(root), max_sum)
        
            
            
        
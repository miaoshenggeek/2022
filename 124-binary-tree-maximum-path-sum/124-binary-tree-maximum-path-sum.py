# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # start from leaf:
        # cal max for each leaf,then max for each parent...then max for root
        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            left=max(helper(node.left),0)
            right=max(helper(node.right),0)
            #the price to start a new path where 'node' is a highest node
            price_newpath=node.val+left+right
            #update max_sum
            max_sum=max(max_sum,price_newpath)
            
            #retrun the max if continue the same path
            return node.val+max(left,right)
        max_sum=float("-inf")
        helper(root)
        return max_sum
            
            
        
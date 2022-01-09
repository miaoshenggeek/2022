# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, A: List[int]) -> Optional[TreeNode]:
       
        return self.buildTree(A, float('inf'))

    def buildTree(self, A, bound):
        if not A or A[0] > bound: return None
        node = TreeNode(A.pop(0))
        node.left = self.buildTree(A, node.val)
        node.right = self.buildTree(A, bound)
        return node
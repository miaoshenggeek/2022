# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    def bstFromPreorder(self, A: List[int]) -> Optional[TreeNode]:
        return self.buildTree(A, float('inf'))

    def buildTree(self, A, bound):
        if not A or A[0] > bound: return None
        node = TreeNode(A.pop(0))
        node.left = self.buildTree(A, node.val)
        node.right = self.buildTree(A, bound)
        return node'''
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:return None
        a=preorder[0]
        root=TreeNode(a)
        #preorder.pop(0)
        idx=0
        if preorder:
            idx=bisect.bisect(preorder,a)
            root.left=self.bstFromPreorder(preorder[1:idx])
            root.right=self.bstFromPreorder(preorder[idx:])
        return root
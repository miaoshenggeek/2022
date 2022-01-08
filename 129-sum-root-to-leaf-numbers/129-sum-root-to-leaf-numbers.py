# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def preorder(root,num=0):
            if not root:
                #print(num)
                return num
            num=num*10+root.val
            if not root.left: return preorder(root.right,num)
            elif not root.right: return preorder(root.left,num)
            else: return preorder(root.right,num)+preorder(root.left,num)
        res=preorder(root,0)
        return res
            
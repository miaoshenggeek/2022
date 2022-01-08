# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:return None
        a=preorder[0]
        root=TreeNode(a)
        preorder.pop(0)
        idx=0
        if preorder:
            prev=preorder[0]
            for i,cur in enumerate(preorder):    
                if prev<a<cur:
                    idx=i
                    break
                prev=cur
        #print(idx,preorder)
        if idx==0 and preorder:
            if preorder[0]>a:root.right=self.bstFromPreorder(preorder[idx:])
            else:root.left=self.bstFromPreorder(preorder)
        else:
            root.left=self.bstFromPreorder(preorder[:idx])
            root.right=self.bstFromPreorder(preorder[idx:])
        return root
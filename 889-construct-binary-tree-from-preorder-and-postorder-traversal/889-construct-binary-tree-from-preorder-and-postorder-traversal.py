# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:return
        root=TreeNode(preorder[0])
        preorder.pop(0)
        postorder.pop()
        if preorder and postorder:
            v=postorder[-1]
            t=preorder[0]
            idx=preorder.index(v)
            idt=postorder.index(t)
            #if idx==0: 
                #root.left=self.constructFromPrePost(preorder,postorder)
            if idt==len(postorder)-1:
                root.right=self.constructFromPrePost(preorder,postorder)
            else:
                root.left=self.constructFromPrePost(preorder[:idx],postorder[:idt+1])
                root.right=self.constructFromPrePost(preorder[idx:],postorder[idt+1:])
        return root
    
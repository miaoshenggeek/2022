# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return 
        stack=deque([root])
        res=[]
        while stack:
            cnt=len(stack)
            cur=[]
            for i in range(cnt):
                node=stack.popleft()
                if node:
                    cur.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            if cur:res.append(cur)
        return res
            
        
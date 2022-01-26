# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack=deque([root])
        res=[]
        level=0
        while stack:
            n=len(stack)
            cur=[]
            for _ in range(n):
                node=stack.popleft()
                if node:
                    cur.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            if level%2==1:
                cur.reverse()
            if cur: res.append(cur)
            level+=1
        return res
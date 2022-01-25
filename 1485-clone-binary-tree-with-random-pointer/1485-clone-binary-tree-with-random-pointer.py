# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:return root
        seen={}
        def helper(node):
            if not node:return node
            if node in seen:
                return seen[node]
            else:
                new=NodeCopy(node.val)
                seen[node]=new   ###method: order matters
                new.left=helper(node.left)
                new.right=helper(node.right)
                new.random=helper(node.random)
                return seen[node]
        return helper(root)
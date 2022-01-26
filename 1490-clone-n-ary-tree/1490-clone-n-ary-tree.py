"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:return
        seen={}
        def helper (root):
            if not root:return
            '''if root in seen:
                return seen[root]'''
            new=Node(root.val)
            seen[root]=new
            for i in root.children:
                new.children.append(helper(i))
            return new
        return helper(root)
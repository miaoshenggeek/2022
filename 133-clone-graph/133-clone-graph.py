"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return node
        seen={}
        
        def helper(node):
            if not node:return
            if node in seen:
                return seen[node]
            else:
                new=Node(node.val)
                seen[node]=new
                new.neighbors=[]
                for i in node.neighbors:
                    #if i not in seen:
                    new.neighbors.append(helper(i))
                    #else:
                    #new.neighbors.append(seen[i])
                return new
        return helper(node)
            
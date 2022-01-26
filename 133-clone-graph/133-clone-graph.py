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
                #new.neighbors=[]
                for i in node.neighbors:
                    new.neighbors.append(helper(i))
                    ####method
                    #For a given node the number of recursive calls = the number of its neighbors
                    #Each recursive call made would return the clone of a neighbor
                    #just worry about ONE such call and let the recursion do the rest. 
                    #always handle the base case or the termination condition of the recursion.
                return new
        return helper(node)
            
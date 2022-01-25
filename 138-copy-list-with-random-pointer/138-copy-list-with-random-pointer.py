"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen={}
        def helper(old) :
            if old:
                if old in seen:
                    return seen[old]
                else:
                    node=Node(old.val)
                    seen[old]=node
                    node.next=helper(old.next)
                    node.random=helper(old.random)
                return node
            return
        return helper(head)
        
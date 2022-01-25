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
        if not head:return head 
        
        def getCopy(node):
            if node:
                if node in seen:
                    return seen[node]
                else:
                    seen[node]=Node(node.val)
                    return seen[node]
            return None
        old=head
        new=Node(old.val)
        seen[old]=new
        
        while old:
            new.random=getCopy(old.random)
            new.next=getCopy(old.next)
            old=old.next
            new=new.next
            
        return seen[head]
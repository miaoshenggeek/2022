# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return 
        if not head.next: return
        if head.next==head:return head
        node=head
        seen=set()
        while node:
            if node.next in seen:
                return node.next
            seen.add(node)
            node=node.next
        return
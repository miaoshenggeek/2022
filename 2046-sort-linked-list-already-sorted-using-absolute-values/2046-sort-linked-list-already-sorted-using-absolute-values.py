# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        prev=dummy=ListNode()
        cur=head
        prev.next=cur
        while cur:
            if cur.val<0 and not dummy.next==cur:
                prev.next=cur.next
                cur.next=dummy.next
                dummy.next=cur
                cur=prev.next
                
            else:    
                cur=cur.next
                prev=prev.next
        return dummy.next
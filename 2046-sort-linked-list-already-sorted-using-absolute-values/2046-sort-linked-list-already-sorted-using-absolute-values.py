# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=cur=head
        cur=cur.next
        while cur:
            temp=cur.next
            if cur.val<0:
                prev.next=temp
                cur.next=head
                head=cur
            else:    
                prev=cur
            cur=temp
        return head
    
                
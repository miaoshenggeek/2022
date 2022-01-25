# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(l1,l2,prev):
            if not l2:return l1
            if not l1:return l2
            new=ListNode()
            
            if l1.val>=l2.val:
                new.val=l2.val
                l2=l2.next
            else:
                new.val=l1.val
                l1=l1.next
            
            new.next=helper(l1,l2,new)
            return new
        prev=ListNode()
        prev.next=helper(l1,l2,prev)
        return prev.next
            
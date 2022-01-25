# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''if not head or not head.next:
            return head
        first=head
        second=head.next
        first.next=self.swapPairs(head.next.next) #second_node.next
        second.next=first
        return second'''
        prev=dummy=ListNode(-1)
        dummy.next=head
        while head and head.next:
            first=head
            second=head.next
            prev.next=second
            first.next=second.next
            second.next=first
            #reinit
            prev=first
            head=first.next
        return dummy.next
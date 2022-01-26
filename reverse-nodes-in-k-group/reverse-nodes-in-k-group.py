# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseNode(node,k):
            prev=None
            cur=node
            while k:
                temp=cur.next
                cur.next=prev
                prev=cur
                cur=temp
                k-=1
            return cur,prev
        count=0
        node=head
        while node and count<k:
            node=node.next
            count+=1
        if count<k:return head
        new_head,prev=reverseNode(head,k)
        head.next=self.reverseKGroup(new_head,k)
        return prev
        
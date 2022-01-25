# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cur=head   
        while cur:
            
            cur.next,prev,cur=prev,cur,cur.next
            
            #print(prev,prev.next)
        return prev

    '''        
    def reverseList_v1(self, head):  # Recursive
        """
        :type head: ListNode
        :rtype: ListNode
        """     
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p '''
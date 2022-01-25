# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findmid(head):
            midPrev=None
            while head and head.next:
                midPrev=midPrev.next if midPrev else head
                head=head.next.next
            mid=midPrev.next
            midPrev.next=None
            return mid
        
        def merge(l,r):
            #print('called')
            tail=dummy=ListNode()
            while l and r:
                if l.val<r.val:
                    tail.next=l
                    l=l.next
                else:
                    tail.next=r
                    r=r.next
                tail=tail.next
            tail.next=l or r
            return dummy.next
                
        if not head or not head.next:return head
        mid=findmid(head)
        #print(mid.val)
        left=self.sortList(head)
        right=self.sortList(mid)
        return merge(left,right)
    
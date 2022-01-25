# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in lists:
            while i:
                arr.append(i.val)
                i=i.next
        arr.sort()
        prev=cur=ListNode()
        for i in arr:
            new=ListNode(i)
            prev.next=new
            prev=prev.next
        return cur.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def brutemergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.nodes=[]  # new object initiation?
        head=point=ListNode(0)
        for i in lists:
            
            while i:
                self.nodes.append(i.val)
                i=i.next
        #print(sorted(self.nodes))
        for x in sorted(self.nodes):
            point.next=ListNode(x)
            point=point.next
        return head.next
        
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            lists[idx] = lists[idx].next
            
            if lists[idx]:
                heapq.heappush(h, (lists[idx].val, idx))
        return head.next
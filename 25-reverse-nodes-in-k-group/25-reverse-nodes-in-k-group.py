# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        l, r : define reversing range
        pre, cur : to reverse, standard reverse linked linked list method
        jump : to connect last node in previous k-group to 1st node in following k-group'''
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
                """
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre
                jump = l
                l = r"""
            else:
                return dummy.next
            '''
            k = 3 for example:

            step 0: a -> b -> c -> (next k-group)

            step 1:      b -> c -> (next k-group)
                              a ---^

            step 2:           c -> (next k-group)
                         b -> a ---^

            step 3:                (next k-group)
                    c -> b -> a ---^

            finish: c -> b -> a -> (next k-group)'''
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''def helper(l1,l2,l3,carry=0):
            if not l1 and not l2 and not carry: return
            
            new=ListNode()
            l3.next=new
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            new.val=(a+b+carry)%10
            carry=(a+b+carry)//10
            if l1:l1=l1.next
            if l2:l2=l2.next
            new.next=helper(l1,l2,new,carry)
            return new
        prev=ListNode()
        prev.next=helper(l1,l2,prev,0)
        return prev.next'''
        if l1 is None: return l2
        if l2 is None: return l1
        l3=ListNode(0)
        cur=l3  
        pas=0
        while l1 and l2 :
            cur.next=ListNode((l1.val+l2.val+pas)%10)
            pas=(l1.val+l2.val+pas)//10
            cur=cur.next
            l1=l1.next
            l2=l2.next
        while l1 :
            cur.next=ListNode((l1.val+pas)%10)
            pas=(pas+l1.val)//10
            cur=cur.next
            l1=l1.next
        while l2 :
            cur.next=ListNode((l2.val+pas)%10)
            pas=(pas+l2.val)//10
            cur=cur.next
            l2=l2.next
        if pas==1:
            cur.next=ListNode(1)
        return l3.next
    

            
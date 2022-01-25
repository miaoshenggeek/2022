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
        return prev.next
        '''
        output = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry = carry//10
        return output.next
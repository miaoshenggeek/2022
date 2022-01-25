# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr[k-1],arr[-k]=arr[-k],arr[k-1]
        ptr=prev=ListNode()
        for i in arr:
            new=ListNode(i)
            prev.next=new
            prev=prev.next
        return ptr.next'''
        
        begin_cnt = 1
        
        begin_node = head
        end_node = None
        
        # finding beginning node
        while begin_cnt < k:
            begin_cnt += 1
            begin_node = begin_node.next
            
        end_1 = head
        end_2 = begin_node.next
        # finding end node
        while end_2 is not None:
            end_1 = end_1.next
            end_2 = end_2.next
        end_node = end_1
    
        tmp = begin_node.val
        begin_node.val = end_node.val
        end_node.val = tmp
        
        return head
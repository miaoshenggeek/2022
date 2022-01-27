# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> int:
        def helper(root,cur_sum):
            nonlocal res
            if not root:return 
            cur_sum+=root.val
            #if cur_sum==t:
            #    res+=1
            res+=h[cur_sum-t] #a path of sum t has occured up till cur node
            h[cur_sum]+=1 #add cur sum for child node processing
            #print(sorted(h.items()),res,cur_sum)
            helper(root.left,cur_sum)
            helper(root.right,cur_sum)
            h[cur_sum]-=1 #remove cur sum for the parallel subtree processing
            #print(res,cur_sum,h)
        res=0
        h=defaultdict(int)
        h[0]=1
        helper(root,0)
        
        return res
        
            
        
                
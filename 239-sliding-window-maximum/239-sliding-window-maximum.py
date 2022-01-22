class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #You want to ensure the deque window only has decreasing elements. 
        #That way, the leftmost element is always the largest.
        q=deque()
        res=[]
        for i,v in enumerate(nums):
            
            if i<k:
                if not q:q.append(i)
                else:
                    while q and nums[q[-1]]<=v:
                        q.pop()
                    q.append(i)
                if i==k-1:res.append(nums[q[0]])
                continue
            
            while q and nums[q[-1]]<=v:
                q.pop()
            q.append(i)
            
            if q[0]<=i-k:q.popleft()
            m=q[0]    
            res.append(nums[m])
        return res
                
                    
        
            
        
        
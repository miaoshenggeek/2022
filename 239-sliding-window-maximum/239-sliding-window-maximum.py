class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Ensure the deque window only has decreasing elements. 
        #So the leftmost element is always the largest.
        q=deque()
        res=[]
        for i,v in enumerate(nums):
            
            while q and nums[q[-1]]<=v:
                q.pop()
                
            q.append(i)
            
            if q[0]<=i-k:q.popleft()
                
            if i>=k-1:res.append(nums[q[0]])
            
        return res
        '''
        d = collections.deque()
        out = []
        
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
                
            d.append(i)
            if d[0] == i - k:  # 存了K+1个元素了
                d.popleft()
            if i >= k - 1:
                out.append(nums[d[0]])
        return out'''
                    
        
            
        
        
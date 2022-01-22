class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N=len(nums)
        P=[0]
        for x in nums:
            P.append(P[-1]+x) #prefix sum
        ans=N+1
        monoq=deque() #record indices of P, P[i] strickly increasing
        for i, Pi in enumerate(P):
            while monoq and Pi<=P[monoq[-1]]:#when find smaller prefix sum
                monoq.pop()   #pop the larger(equal) prefix sum
            while monoq and Pi-P[monoq[0]]>=k:
                ans =min(ans,i-monoq.popleft()) #P[monoq[0] is smallest in P
            monoq.append(i)   #add cur
        return ans if ans<N+1 else -1
    """
    Why keep the deque increase?
    If B[i] <= B[d.back()] and moreover we already know that i > d.back(),
    it means that compared with d.back(),
    B[i] can help us make the subarray length shorter and sum bigger. 
    So no need to keep d.back() in our deque."""
            
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        d=deque([[-1,0]])
        cur=0
        res=float("inf")
        for i,v in enumerate(nums):
            cur+=v
            while d and cur-d[0][1]>=target:
                res=min(res,i-d.popleft()[0])
            d.append([i,cur])
        return res if res<float("inf") else 0
                
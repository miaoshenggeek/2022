class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        end=1
        cur=1-nums[start]
        res=k
        n=len(nums)
        while end<n:
           
            while (cur==k and nums[end]==0) or cur>k:
                cur=cur-(1-nums[start])
                start+=1   
            if nums[end]==0 and cur<k:
                cur+=1   
            end+=1
            res=max(res,end-start)
            #print(cur,res,end,start)
        return res
        
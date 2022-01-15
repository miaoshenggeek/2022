class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        diff = float('inf')
        for i, v1 in enumerate(nums):
            for j,v2 in enumerate(nums[i+1:]):
                v3=target-v1-v2
                hi=bisect_right(nums,v3,i+j+2)
                lo=hi-1
                if hi<len(nums) and abs(v3-nums[hi])<abs(diff):
                    diff=v3-nums[hi]
                if lo>i+1+j and abs(v3-nums[lo])<abs(diff):
                    diff=v3-nums[lo]
                if diff==0:
                    break
        return target-diff
        
        
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        diff=float("inf")
        for i,v1 in enumerate(nums):
            lo=i+1
            hi=n-1
            while lo<hi:
                test=v1+nums[lo]+nums[hi]
                if abs(diff)>abs(target-test):
                    diff=target-test
                if test==target:
                    return target
                elif test<target:
                    lo+=1
                else:
                    hi-=1
        return target-diff
                
            
        
        
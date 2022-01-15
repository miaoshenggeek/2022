class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        s=1
        for i in nums[:-1]:
            s*=i
            prefix.append(s)
        print(prefix)
        r=1
        for i in range(len(nums)-1,-1,-1):
            prefix[i]*=r
            r*=nums[i]
            #print(i,-i-2)
        return prefix
            
        
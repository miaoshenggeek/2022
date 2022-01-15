class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        s=1
        for i in nums:
            s*=i
            prefix.append(s)
        suffix=[1]
        d=1
        for i in nums[::-1]:
            d*=i
            suffix.append(d)
        #print(prefix)
        #print(suffix)
        res=[]
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[-i-2])
            #print(i,-i-2)
        return res
            
        
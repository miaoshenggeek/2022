class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=set()
        for i,v in enumerate(nums):
            if v%10001<n:
                nums[v%10001]=nums[v%10001]+10001
                #print(nums)
        
        for i in range(n):
            if nums[i]<10001:
                return i
        return n

    #[2,0]